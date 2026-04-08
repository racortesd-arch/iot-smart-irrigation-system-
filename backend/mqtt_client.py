# Simplified example - production code may differ

import ssl
import paho.mqtt.client as mqtt
import time 
import threading    
import json
from db import get_conn

UMBRAL_HUMEDAD = 1800
TIEMPO_RIEGO = 2  # segundos
COOLDOWN = 45 * 60  # 45 minutos
BATERIA_MINIMA = 3.5
TIEMPO_SECO_MIN = 60 * 60  # 1 hora
CORRIENTE_MIN = 0.3
CORRIENTE_MAX = 0.7

inicio_sequedad = None
modo = "MANUAL" 
ultimo_riego = 0
bomba_encendida = False
mqtt_client = None 


def log_decision(decision, motivo):
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO decisiones (ts, decision, motivo)
        VALUES (NOW(), %s, %s)
    """, (decision, motivo))

    conn.commit()
    cur.close()
    conn.close()    

def crear_alarma(tipo, mensaje, nivel="WARNING"):
    conn = get_conn()
    cur = conn.cursor()

    # ❗ evitar spam (últimos 5 minutos)
    cur.execute("""
        SELECT 1 FROM alarmas
        WHERE tipo = %s
        AND ts > NOW() - INTERVAL '5 minutes'
        LIMIT 1
    """, (tipo,))

    existe = cur.fetchone()

    if existe:
        cur.close()
        conn.close()
        return

    cur.execute("""
        INSERT INTO alarmas (ts, tipo, mensaje, nivel, activa)
        VALUES (NOW(), %s, %s, %s, TRUE)
    """, (tipo, mensaje, nivel))

    conn.commit()
    cur.close()
    conn.close()

def on_connect(client, userdata, flags, rc):
    print("Conectado a MQTT con código:", rc)
    client.subscribe("riego/#")

def publicar_riego(client, estado):
    client.publish("riego/bomba/cmd", estado)

def alerta(msg):
    print(f"⚠️ ALERTA: {msg}")

modo_cache = "MANUAL"
last_modo_check = 0

def get_modo_cached():
    global modo_cache, last_modo_check

    ahora = time.time()

    if ahora - last_modo_check > 10:
        conn = get_conn()
        cur = conn.cursor()

        cur.execute("SELECT modo FROM modo ORDER BY ts DESC LIMIT 1")
        row = cur.fetchone()

        if row:
            modo_cache = row[0]

        cur.close()
        conn.close()

        last_modo_check = ahora

    return modo_cache

def procesar_sensor(client, data):
    global inicio_sequedad, ultimo_riego

    modo_actual = get_modo_cached()
    if modo_actual != "AUTO":
        print("⛔ Modo MANUAL activo")
        return
    print(f"DEBUG MODO ACTUAL: {modo}")
    humedad = data.get("humedad")
    bateria = data.get("bateria")

    ahora = time.time()

    print(f"📥 Humedad: {humedad} | Batería: {bateria}")

    if bateria < BATERIA_MINIMA:
        alerta("Batería baja, no se riega")
        crear_alarma("LOW_BATTERY", "Batería baja, no se riega","WARNING")
        return

    if ahora - ultimo_riego < COOLDOWN:
        print("⏳ En cooldown")
        return

    # 🌵 detectar sequedad por tiempo
    if humedad > UMBRAL_HUMEDAD:
        if inicio_sequedad is None:
            inicio_sequedad = ahora
            print("🌵 Inicio sequedad")
        else:
            tiempo_seco = ahora - inicio_sequedad
            print(f"🌵 Seco por {tiempo_seco:.0f} seg")

            if tiempo_seco >= TIEMPO_SECO_MIN:
                activar_riego(client)
                log_decision(
                    "RIEGO_ON",
                    f"Humedad baja por {tiempo_seco} segundos"
                )

    else:
        if inicio_sequedad is not None:
            print("💧 Se recuperó humedad")
        inicio_sequedad = None

def activar_riego(client):
    global ultimo_riego, inicio_sequedad, bomba_encendida    

    if get_modo_cached() != "AUTO":
        print("⛔ Cambio a MANUAL, no se riega")
        return

    print("💧 Riego ON")
    publicar_riego(client, "ON")

    bomba_encendida = True
    threading.Timer(TIEMPO_RIEGO, apagar_riego, [client]).start()

    ultimo_riego = time.time()
    inicio_sequedad = None


def apagar_riego(client):
    print("🛑 Riego OFF")
    publicar_riego(client, "OFF")


def on_message(client, userdata, msg):
    global bomba_encendida

    payload = msg.payload.decode()

    print(f"TOPIC: '{msg.topic}'")
    print(f"PAYLOAD: {payload}")

    conn = get_conn()
    cur = conn.cursor()


    try:
        if msg.topic == "riego/sensores":
            data = json.loads(payload)
            #print(f"data: {data}")
            cur.execute(
                "INSERT INTO sensores (ts, humedad, bateria, peso) VALUES (NOW(), %s, %s, %s)",
                (data["humedad"], data["bateria"], data["peso"])
            )

            procesar_sensor(client, data)
       
        conn.commit()

    except Exception as e:
        print("Error:", e)
        conn.rollback()  

    finally:
        cur.close()
        conn.close()

def start_mqtt():
    global mqtt_client

    mqtt_client = mqtt.Client()

    mqtt_client.tls_insecure_set(False)
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message

    mqtt_client.connect("localhost", 8883)

    mqtt_client.loop_start()

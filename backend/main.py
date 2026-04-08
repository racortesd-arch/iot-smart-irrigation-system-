# Simplified example - production code may differ

from fastapi import FastAPI
import mqtt_client
import time
from db import get_conn
from fastapi.middleware.cors import CORSMiddleware
from mqtt_client import log_decision

@app.on_event("startup")
def startup():
    mqtt_client.start_mqtt()

@app.get("/sensores")
def get_sensores():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT * FROM sensores ORDER BY ts DESC LIMIT 10")
    data = cur.fetchall()

    cur.close()
    conn.close()
    return data

@app.get("/bomba/evento")
def get_eventos():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT * FROM eventos_bomba ORDER BY ts DESC LIMIT 10")
    data = cur.fetchall()

    cur.close()
    conn.close()
    return data

@app.get("/bomba/corriente")
def get_corriente():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT * FROM corriente ORDER BY ts DESC LIMIT 10")
    data = cur.fetchall()

    cur.close()
    conn.close()
    return data

@app.get("/estado")
def estado():
    return {
        "modo": mqtt_client.modo,
        "bomba": "ON" if mqtt_client.bomba_encendida else "OFF",
        "timestamp": time.time()
    }

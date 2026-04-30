# 🪴 Smart Irrigation IoT System

IoT-based smart irrigation system for real-time soil moisture monitoring and automated watering.
The system integrates an ESP32-C3 with soil moisture sensing, solar-powered energy management, and water actuation, combined with an end-to-end IoT architecture including MQTT communication, backend processing, database storage, and real-time visualization dashboards.

## Architecture 🏗️
ESP32-C3 → MQTT Broker → Backend (Python) → PostgreSQL → Grafana Dashboard

## Technologies ⚙️
- ESP32C3
- MQTT
- Python (Backend)
- PostgreSQL
- Grafana
- Linux (VPS)
- Solar power system (18650 battery + CN3065)

## Features 🔧

- Real-time soil moisture monitoring
- Automated irrigation control
- Solar-powered operation with battery management
- Deep sleep optimization for ultra-low power consumption
- Remote configuration of irrigation parameters (threshold & timing)
- Remote device control (sleep/wake commands)
- Data storage and historical analysis
- Real-time visualization via Grafana dashboards

## Advanced Control & Power Optimization ⚡

The system implements deep sleep strategies to significantly reduce power consumption, enabling long-term off-grid operation using solar energy.

Additionally, key irrigation parameters can be remotely configured from the Grafana dashboard:

- Soil moisture threshold
- Irrigation timing
- Device operational state (sleep / wake)

This allows dynamic system tuning without physical access to the device, improving flexibility and maintainability in real-world deployments.

##  System Design 🧠

Simplified system architecture and hardware design. Detailed hardware schematics available upon request.

<img width="690" height="521" alt="Diagrama Riego" src="https://github.com/user-attachments/assets/686bd12c-941e-4f73-852d-a8d56038611a" />

## Hardware Setup 📸

<img src="https://github.com/user-attachments/assets/12749245-084e-4fbd-b028-a1d7d3c41954" width="200">
<img src="https://github.com/user-attachments/assets/f4d61749-9b46-4b0d-a4ca-0437f6fc82be" width="200">
<img src="https://github.com/user-attachments/assets/8ad94f9b-3778-433b-b890-fe4d7f1479df" width="200">
<img src="https://github.com/user-attachments/assets/edbb7113-1118-487c-8050-07ab52aad6c8" width="200">

## Data Visualization 📊

Real-time monitoring of soil moisture and irrigation events using Grafana dashboards.
<img width="2160" height="1048" alt="Grafanasensores" src="https://github.com/user-attachments/assets/98c9e23c-6e44-4316-bb16-73a4d18ba16e" />
<img width="2145" height="1084" alt="grafanabomba" src="https://github.com/user-attachments/assets/97a8849a-569b-47b2-ae96-0de9cda67bcd" />
<img width="2159" height="1028" alt="Grafaestados" src="https://github.com/user-attachments/assets/aeee92b2-2163-4b72-bf8a-33d7ce1f1e18" />

## System Schematic 🔌

<img width="1553" height="1071" alt="Prototipo2" src="https://github.com/user-attachments/assets/f23e1e25-987a-428b-b915-164821843df9" />

## Technical Challenges 🧪

- Reliable MQTT communication
- Power management using solar energy
- Sensor calibration and accuracy
- System stability in real-world conditions

## Impact 🚀

- Autonomous irrigation system with minimal human intervention
- Real-time monitoring and remote control
- Designed for low-power off-grid operation

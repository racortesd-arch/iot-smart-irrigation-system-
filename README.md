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
- Solar-powered operation
- Data storage and historical analysis
- Remote visualization via dashboards
  
##  System Design 🧠

Simplified system architecture and hardware design. Detailed hardware schematics available upon request.

<img width="700" height="600" alt="Diagrama Riego" src="https://github.com/user-attachments/assets/b938fdcd-0543-498e-886b-fafcb8ff6733" />

## Hardware Setup 📸

<img src="https://github.com/user-attachments/assets/12749245-084e-4fbd-b028-a1d7d3c41954" width="200">
<img src="https://github.com/user-attachments/assets/f4d61749-9b46-4b0d-a4ca-0437f6fc82be" width="200">
<img src="https://github.com/user-attachments/assets/8ad94f9b-3778-433b-b890-fe4d7f1479df" width="200">
<img src="https://github.com/user-attachments/assets/edbb7113-1118-487c-8050-07ab52aad6c8" width="200">

## Data Visualization 📊

Real-time monitoring of soil moisture and irrigation events using Grafana dashboards.

<img width="800" height="800" alt="Dashboardbomba" src="https://github.com/user-attachments/assets/e7268f44-a4a2-4cbd-a78a-b532f5710108" />
<img width="800" height="800" alt="Grafanasensores" src="https://github.com/user-attachments/assets/b41435f9-f250-4495-b731-147311f7838f" />
<img width="800" height="800" alt="grafanabomba" src="https://github.com/user-attachments/assets/8288af93-57f2-400a-9498-63d5b67a90c0" />

## Technical Challenges 🧪

- Reliable MQTT communication
- Power management using solar energy
- Sensor calibration and accuracy
- System stability in real-world conditions

## Impact 🚀

- Autonomous irrigation system with minimal human intervention
- Real-time monitoring and remote control
- Designed for low-power off-grid operation

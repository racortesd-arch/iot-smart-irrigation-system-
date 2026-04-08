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
- 
##  System Design 🧠

Simplified system architecture and hardware design. Detailed hardware schematics available upon request.

<img width="700" height="600" alt="Diagrama Riego" src="https://github.com/user-attachments/assets/8f35bf7d-b2b8-4c90-b18a-08df1c0fe54f" />

## Hardware Setup 📸

<img src="https://github.com/user-attachments/assets/6b49ac93-49c2-4cb1-af2d-4c11ef0f1db3" width="200">
<img src="https://github.com/user-attachments/assets/0f8f8149-e4af-40d0-b1cc-ea1e92754387" width="200">
<img src="https://github.com/user-attachments/assets/5157808c-ed46-443b-a076-8030a7b0e2fb" width="200">
<img src="https://github.com/user-attachments/assets/a6f9d39f-f86b-444a-99ec-0f76e1701813" width="200">

## Data Visualization 📊

Real-time monitoring of soil moisture and irrigation events using Grafana dashboards.

<img width="800" height="800" alt="Grafanasensores" src="https://github.com/user-attachments/assets/ded0425f-a8ad-4d5e-bc27-53348169678e" />
<img width="800" height="800" alt="grafanabomba" src="https://github.com/user-attachments/assets/093d78cd-5b7a-479d-930d-9ef70bb83ccf" />
<img width="800" height="800" alt="Dashboardbomba" src="https://github.com/user-attachments/assets/0139c840-0ea1-4c3e-8205-349cca616d90" />


## Technical Challenges 🧪

- Reliable MQTT communication
- Power management using solar energy
- Sensor calibration and accuracy
- System stability in real-world conditions

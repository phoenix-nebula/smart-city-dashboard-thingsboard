import paho.mqtt.client as mqtt
import json
import time
import random

# Richard's ThingsBoard device tokens
TOKENS = {
    "WeatherSensor": "These Tokens",
    "SafetySensor": "are",
    "TrafficSensor": "private",
    "UtilitySensor": "Thank you",
    "AirQualitySensor": "He he he he"
}

# Create MQTT clients for each device
clients = {}
for device, token in TOKENS.items():
    client = mqtt.Client()
    client.username_pw_set(token)
    client.connect("thingsboard.cloud", 1883, 60)
    clients[device] = client

while True:
    # WeatherSensor
    weather_data = {
        "temperature": round(random.uniform(24, 38), 2),
        "humidity": round(random.uniform(50, 95), 2),
        "wind_speed": round(random.uniform(0, 15), 2),
        "rainfall": round(random.uniform(0, 50), 2),
        "lat": 51.5074,
        "lon": -0.1270
    }
    clients["WeatherSensor"].publish("v1/devices/me/telemetry", json.dumps(weather_data))
    print("WeatherSensor telemetry:", weather_data)

    # SafetySensor
    safety_data = {
        "flood_level": round(random.uniform(0, 5), 2),
        "noise_db": random.randint(30, 120)
    }
    clients["SafetySensor"].publish("v1/devices/me/telemetry", json.dumps(safety_data))
    print("SafetySensor telemetry:", safety_data)

    # TrafficSensor
    traffic_data = {
        "people_count": random.randint(0, 200),
        "vehicle_count": random.randint(0, 100)
    }
    clients["TrafficSensor"].publish("v1/devices/me/telemetry", json.dumps(traffic_data))
    print("TrafficSensor telemetry:", traffic_data)

    # UtilitySensor
    utility_data = {
        "power_kwh": round(random.uniform(100, 500), 2),
        "water_usage": round(random.uniform(50, 300), 2),
        "power_status": random.choice([True, False])
    }
    clients["UtilitySensor"].publish("v1/devices/me/telemetry", json.dumps(utility_data))
    print("UtilitySensor telemetry:", utility_data)

    # AirQualitySensor
    air_data = {
        "aqi": random.randint(50, 400),
        "co2": random.randint(400, 2000)
    }
    clients["AirQualitySensor"].publish("v1/devices/me/telemetry", json.dumps(air_data))
    print("AirQualitySensor telemetry:", air_data)

    print("Telemetry sent to all 5 devices...\n")
    time.sleep(5)

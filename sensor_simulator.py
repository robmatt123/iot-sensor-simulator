import json
import time
import random
import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
TOPIC = "greenfield/serra01/temperature"

client = mqtt.Client()
client.connect(BROKER, PORT)

def generate_temperature():
    base = 24
    variation = random.uniform(-2, 2)
    return round(base + variation, 2)

while True:

    payload = {
        "sensor_id": "serra01_temp",
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "type": "temperature",
        "value": generate_temperature(),
        "unit": "C"
    }

    client.publish(TOPIC, json.dumps(payload), qos=1)
    print("Sent:", payload)

    time.sleep(3)

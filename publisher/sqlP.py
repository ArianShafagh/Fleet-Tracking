import paho.mqtt.client as mqtt
import random
import time
import json

broker_address = "mqtt"  # or "localhost"
port = 1883
topic = "fleet/speed"

client = mqtt.Client()
client.connect(broker_address, port)

def get_status(speed):
    if speed > 120:
        return "overspeed"
    elif speed < 30:
        return "lowspeed"
    return "normal"

car_counter = 1

while True:
    car_id = f"CAR_{car_counter}"
    speed = random.randint(0, 150)
    status = get_status(speed)

    data = {
        "car_id": car_id,
        "speed": speed,
        "status": status
    }

    client.publish(topic, json.dumps(data))
    print(f"Published: {data}")

    car_counter += 1
    time.sleep(3)

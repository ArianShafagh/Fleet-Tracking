import paho.mqtt.client as mqtt
import random
import time
import json

broker_address = "mqtt" # "localhost"
port = 1883
topic = "fleet/location"

client = mqtt.Client()
client.connect(broker_address, port)

car_counter = 1

def generate_coordinates():
    lat = round(random.uniform(37.5, 37.6), 6)
    lon = round(random.uniform(15.5, 15.8), 6)
    return lat, lon

while True:
    car_id = f"CAR_{car_counter}"
    latitude, longitude = generate_coordinates()

    data = {
        "car_id": car_id,
        "latitude": latitude,
        "longitude": longitude
    }
    
    print("Publishing to fleet/location:", data)
    client.publish(topic, json.dumps(data))
    print(f"Published to MongoDB topic: {data}")

    car_counter += 1
    time.sleep(3)

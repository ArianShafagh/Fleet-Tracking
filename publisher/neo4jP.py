import paho.mqtt.client as mqtt
import random
import time
import json

broker_address = "mqtt"
port = 1883
topic = "fleet/route"

client = mqtt.Client()
client.connect(broker_address, port)

car_counter = 1
points = ["Messina", "Catania", "Palermo", "Syracuse", "Enna", "Ragusa"]

while True:
    car_id = f"CAR_{car_counter}"
    from_point, to_point = random.sample(points, 2)

    data = {
        "car_id": car_id,
        "from": from_point,
        "to": to_point
    }

    client.publish(topic, json.dumps(data))
    print(f"Published to Neo4j topic: {data}")

    car_counter += 1
    time.sleep(3)

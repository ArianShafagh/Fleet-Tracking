import paho.mqtt.client as mqtt
from pymongo import MongoClient
import json
import sys
import time

try:
    mongo_client = MongoClient("mongodb://mongodb:27017/", serverSelectionTimeoutMS=3000)
    mongo_client.server_info() 
    print("Connected to MongoDB")
except Exception as e:
    print("MongoDB connection failed:", e)
    sys.exit(1)

db_name = "fleet_data"
collection_name = "car_locations"
db = mongo_client[db_name]
collection = db[collection_name]
print(f"Using database '{db_name}' and collection '{collection_name}'")

def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        car_id = payload['car_id']
        latitude = payload['latitude']
        longitude = payload['longitude']

        document = {
            "car_id": car_id,
            "latitude": latitude,
            "longitude": longitude
        }
        print("Received message:", document)
        collection.insert_one(document)
        print("Inserted into MongoDB")
    except Exception as e:
        print("Error processing message:", e)

client = mqtt.Client()
while True:
    try:
        client.connect("mqtt", 1883)
        print("Connected to MQTT broker")
        break
    except Exception as e:
        print("MQTT connection failed, retrying in 3s:", e)
        time.sleep(3)

client.subscribe("fleet/location")
client.on_message = on_message
print("Subscriber is listening to 'fleet/location'...")
client.loop_forever()

import paho.mqtt.client as mqtt
import mysql.connector
import json
import time

while True:
    try:
        db = mysql.connector.connect(
            host="mysql",          
            user="root",
            password="root",
            database="fleet_data"
        )
        print("✅ Connected to MySQL")
        break
    except mysql.connector.Error as err:
        print("❌ MySQL connection failed, retrying in 3s...", err)
        time.sleep(3)

cursor = db.cursor()

def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        car_id = payload['car_id']
        speed = payload['speed']
        status = payload['status']

        query = "INSERT INTO fleet_tracking (car_id, speed, status) VALUES (%s, %s, %s)"
        values = (car_id, speed, status)
        cursor.execute(query, values)
        db.commit()

        print(f"✅ Inserted: {car_id}, {speed}, {status}")
    except Exception as e:
        print("❌ Error processing message:", e)

client = mqtt.Client()

while True:
    try:
        client.connect("mqtt", 1883)
        print("✅ Connected to MQTT broker")
        break
    except Exception as e:
        print("❌ MQTT connection failed, retrying in 3s...", e)
        time.sleep(3)

client.subscribe("fleet/speed")
client.on_message = on_message

print("🟢 Subscriber is listening to 'fleet/speed'...")
client.loop_forever()

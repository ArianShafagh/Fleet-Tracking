import paho.mqtt.client as mqtt
import json
import requests

neo4j_url = "http://neo4j:7474/db/neo4j/tx/commit"
neo4j_user = "neo4j"
neo4j_pass = "password"

def send_to_neo4j(car_id, from_point, to_point):
    query = {
        "statements": [
            {
                "statement": """
                    MERGE (a:Point {name: $from})
                    MERGE (b:Point {name: $to})
                    MERGE (v:Vehicle {car_id: $car_id})
                    MERGE (v)-[:TO]->(b)
                    MERGE (v)-[:FROM]->(a)
                """,
                "parameters": {
                    "from": from_point,
                    "to": to_point,
                    "car_id": car_id
                }
            }
        ]
    }

    response = requests.post(
        neo4j_url,
        auth=(neo4j_user, neo4j_pass),
        headers={"Content-Type": "application/json"},
        data=json.dumps(query)
    )

    if response.status_code == 200:
        print(f"Neo4j insertion success for {car_id}")
    else:
        print(f"Neo4j error: {response.status_code} - {response.text}")

def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        car_id = payload['car_id']
        from_point = payload['from']
        to_point = payload['to']

        send_to_neo4j(car_id, from_point, to_point)

    except Exception as e:
        print("Error processing message:", e)

client = mqtt.Client()
client.connect("mqtt", 1883)
client.subscribe("fleet/route")
client.on_message = on_message

print("Neo4j Subscriber is listening to 'fleet/route'...")
client.loop_forever()

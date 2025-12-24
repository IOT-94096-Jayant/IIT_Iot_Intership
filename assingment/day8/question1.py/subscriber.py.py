import paho.mqtt.client as mqtt
import mysql.connector

# MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="smarthome"
)
cursor = db.cursor()

def on_message(client, userdata, msg):
    topic = msg.topic
    value = float(msg.payload.decode())

    if topic == "sensor/ldr":
        sensor = "LDR"
    elif topic == "sensor/lm35":
        sensor = "LM35"

    query = "INSERT INTO sensor_data(sensor_type, value) VALUES (%s, %s)"
    cursor.execute(query, (sensor, value))
    db.commit()

    print(f"Stored {sensor}: {value}")

client = mqtt.Client()
client.on_message = on_message

client.connect("localhost", 1883)

client.subscribe("sensor/ldr")
client.subscribe("sensor/lm35")

client.loop_forever()
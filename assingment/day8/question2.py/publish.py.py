import paho.mqtt.client as mqtt
import time
import random

broker = "localhost"
port = 1883

client = mqtt.Client()
client.connect(broker, port)

while True:
    ldr_value = random.randint(100, 900)     # Light intensity
    temp_value = random.uniform(20, 35)      # Temperature

    client.publish("sensor/ldr", ldr_value)
    client.publish("sensor/lm35", temp_value)

    print("Published LDR:", ldr_value)
    print("Published TEMP:", temp_value)

    time.sleep(5)
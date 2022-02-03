import paho.mqtt.client as mqtt
import time
import random

mqttBroker = "test.mosquitto.org"
client = mqtt.Client("Sensor_1")
client.connect(mqttBroker)

while True:
  status = random.randint(0, 1)
  client.publish("Sensor_1", status)
  print("Sensor 1 status ", status)
  time.sleep(3)
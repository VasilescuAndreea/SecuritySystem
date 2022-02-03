import paho.mqtt.client as mqtt
import time
import random

mqttBroker = "test.mosquitto.org"
client = mqtt.Client("Sensor_2")
client.connect(mqttBroker)

while True:
  status = random.randint(0, 1)
  client.publish("Sensor_2", status)
  print("Sensor 2 status ", status)
  time.sleep(3)
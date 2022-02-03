import paho.mqtt.client as mqtt
import time
import base64

mqttBroker = "test.mosquitto.org"
client = mqtt.Client("CCTV")
client.connect(mqttBroker)

def on_message(client, userdata, message):
  print("Am primit request")
  with open("../imgs/cctv-img.jpg", "rb") as imageFile:
    img = base64.b64encode(imageFile.read())

    foo = mqtt.Client("CCTV_Temp")
    foo.connect("test.mosquitto.org")
    foo.publish("CCTV/requestSent", img.decode("utf-8"))

client.on_message = on_message

client.loop_start()

while True:

  client.subscribe("CCTV/request")

client.loop_stop()
import paho.mqtt.client as mqtt
import time
import json
from datetime import datetime

mqttBroker = "test.mosquitto.org"
client = mqtt.Client("Server")
client.connect(mqttBroker)

def requestImage():
  print("Ai cerut eu n am facut")
  client.publish("CCTV/request")

def readJson(file):
  with open(file) as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()
  return jsonObject

def writeJson(jsonObject, file):
  with open(file, "w") as jsonFile:
    json.dump(jsonObject, jsonFile)
    jsonFile.close()

def writeAlarmStarted():
  jsonObject = readJson('logs.json')
  jsonObject["logs"].append(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
  writeJson(jsonObject, 'logs.json')

def mqttStart():

  def on_message(client, userdata, message):
    msg = str(message.payload.decode("utf-8"))
    jsonObject = readJson('currentStatus.json')
    if message.topic == "Sensor_1":
      jsonObject["sensors"][0] = int(msg)
      if int(msg) == 1 and jsonObject['alarmStatus'] == True:
        writeAlarmStarted()
    if message.topic == "Sensor_2":
      jsonObject["sensors"][1] = int(msg)
      if int(msg) == 1 and jsonObject['alarmStatus'] == True:
        writeAlarmStarted()
    if message.topic == "CCTV/requestSent":
      jsonObject["cctvLastImg"] = msg
    
    writeJson(jsonObject, 'currentStatus.json')
    

  client.on_message = on_message

  client.loop_start()

  while True:

    client.subscribe("Sensor_1")
    client.subscribe("Sensor_2")
    client.subscribe("CCTV/requestSent")

  client.loop_stop()

if __name__ == "__main__":
  client.publish("CCTV/request")
  mqttStart()

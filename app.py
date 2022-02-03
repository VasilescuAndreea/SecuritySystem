import json
from flask import Flask
from flask import jsonify
import paho.mqtt.client as mqtt
from main import readJson, writeJson
import time

my_app = Flask("Rest API")

@my_app.route("/")
def main_page():
  return jsonify("Security system is up and running.")

@my_app.route("/cctv")
def cctv_now():
  img = readJson('currentStatus.json')['cctvLastImg']
  return '<img src="data:image/jpg;base64, {}" />'.format(img)

@my_app.route("/getCurrentCCTV")
def get_current_cctv():
  foo = mqtt.Client("RestApi")
  foo.connect("test.mosquitto.org")
  foo.publish("CCTV/request")
  time.sleep(3)
  jsonObject = readJson('currentStatus.json')
  return jsonify(jsonObject['cctvLastImg'])

def alarmInJson(mode):
  jsonObject = readJson('currentStatus.json')
  jsonObject['alarmStatus'] = mode
  writeJson(jsonObject, 'currentStatus.json')

@my_app.route("/alarm/<mode>")
def alarm_disarm(mode):
  if mode =='alarm':
    alarmInJson(True)
    return jsonify(True)
  elif mode =='disarm':
    alarmInJson(False)
    return jsonify(False)
  return jsonify('Error')

@my_app.route("/logsAlarm")
def logs_alarm():
  jsonObject = readJson('logs.json')
  return jsonify(jsonObject)

@my_app.route("/getStatus")
def get_status():
  jsonObject = readJson('currentStatus.json')
  return jsonify(jsonObject)


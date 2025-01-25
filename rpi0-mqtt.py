#!./venv/bin/python

import os
import time
import paho.mqtt.client as mqtt

# MQTT 설정
MQTT_BROKER = "192.168.35.14"
MQTT_PORT = 1883
MQTT_TOPIC = "home/rpi0/temperature/cpu"

def get_cpu_temperature():
    res = os.popen("vcgencmd measure_temp").readline()
    return float(res.replace("temp=", "").replace("'C\n", ""))

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

client = mqtt.Client()
client.on_connect = on_connect
client.connect(MQTT_BROKER, MQTT_PORT, 60)

client.loop_start()

try:
    while True:
        cpu_temp = get_cpu_temperature()
        client.publish(MQTT_TOPIC, cpu_temp)
        time.sleep(10)
except KeyboardInterrupt:
    client.loop_stop()
    client.disconnect()
    
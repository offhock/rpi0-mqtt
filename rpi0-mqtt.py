#!./venv/bin/python

import os
import time
import paho.mqtt.client as mqtt

# MQTT 설정
MQTT_BROKER = "192.168.35.14"
MQTT_PORT = 1883
MQTT_TOPIC1 = "homeassistant/rpi0-0/cpu/temperature"
MQTT_TOPIC2 = "homeassistant/rpi0-0/cpu/frequency"
def get_cpu_temperature():
    res = os.popen("cat /sys/class/thermal/thermal_zone0/temp").readline()
    return round(float(int(res)/1000),1)

def get_cpu_frequency():
    res = os.popen("cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq").readline()
    return round(float(int(res)/1000),1)

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

client = mqtt.Client()
client.on_connect = on_connect
client.username_pw_set("user","passwd")
client.connect(MQTT_BROKER, MQTT_PORT, 60)


client.loop_start()

try:
    while True:
        cpu_temp = get_cpu_temperature()
        cpu_freq = get_cpu_frequency()
        client.publish(MQTT_TOPIC1, cpu_temp)
        client.publish(MQTT_TOPIC2, cpu_freq)
        time.sleep(10)
except KeyboardInterrupt:
    client.loop_stop()
    client.disconnect()

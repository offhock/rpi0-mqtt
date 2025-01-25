#!/bin/bash

ECHO="echo"

if $1; then
    ECHO=""
fi


ECHO sudo ln -s $(pwd)/rpi0-mqtt.service /etc/systemd/system/rpi0-mqtt.service
ECHO sudo systemctl daemon-reload
ECHO sudo systemctl enable rpi0-mqtt.service
ECHO sudo systemctl start rpi0-mqtt.service
ECHO sudo systemctl status rpi0-mqtt.service

#!/bin/bash

sudo apt-get update
sudo apt-get install -y python3 python3-pip

echo "current directory: $PWD"

echo "Installing virtualenv"
python3 -m venv venv
echo "Installing paho-mqtt"
source venv/bin/activate
pip3 install paho-mqtt


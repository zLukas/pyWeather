#! /bin/bash

apt-get update
apt-get upgrade
apt-get install -y git python3-pip3

pip3 install -r requirements.txt

git clone https://github.com/zLukas/pyWeather.git 
cd pyWeather
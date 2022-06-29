#! /bin/bash

nohup python3 git/pyWeather/station.py > /dev/null 2>&1 & echo $! > run.pid
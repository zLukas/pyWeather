#! /bin/bash

nohup python3 git/pyWeather/station.py > log.txt 2>&1 & echo $! > run.pid
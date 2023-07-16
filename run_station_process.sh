#! /bin/bash

nohup python3 station.py > log.txt 2>&1 & echo $! > run.pid
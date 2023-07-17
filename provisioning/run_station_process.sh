#! /bin/bash

# check for existing processes
if [ -f "run.pid" ]
then
    kill -9 "$(cat run.pid)"
fi

# run new instance
nohup python3 ../station.py > log.txt 2>&1 & echo $! > run.pid
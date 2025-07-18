# #! /bin/bash

# # check for existing processes
# if [ -f "run.pid" ]
# then
#     kill -9 "$(cat run.pid)"
# fi

# # run new instance
# nohup python3 ../station.py > log.txt 2>&1 & echo $! > run.pid

#! /bin/bash



LIB_TARGET="/usr/local/lib/pyWeather"
mkdir -p ${LIB_TARGET}
cp -r ../pyWeather/* ${LIB_TARGET}
# Create a systemd service for the weather station
# This script assumes you have the necessary permissions to create systemd services
# and that you have Python 3 installed.
# Adjust the paths as necessary for your environment.
#!/bin/bash 


SERVICE_NAME=station
SERVICE_FILE="/etc/systemd/system/${SERVICE_NAME}.service"
PYTHON_PATH=$(which python3)
WORKDIR=$(cd "$(dirname "$0")/.." && pwd)

# Create systemd service file
sudo bash -c "cat > $SERVICE_FILE" <<EOL
[Unit]
Description=Weather Station Service
After=network.target

[Service]
Type=simple
WorkingDirectory=${LIB_TARGET}
ExecStart=${PYTHON_PATH} ${LIB_TARGET}/station.py
Restart=on-failure
User=$(whoami)

[Install]
WantedBy=multi-user.target
EOL

# Reload systemd, enable and start the service
sudo systemctl daemon-reload
sudo systemctl enable $SERVICE_NAME
sudo systemctl restart $SERVICE_NAME

echo "Service '$SERVICE_NAME' installed and started."
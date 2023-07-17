#! /bin/bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
URL="${1}"

cd ${SCRIPT_DIR}/..

python3 database.py --url ${URL}
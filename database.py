from sqlite import SqliteDataBase
import requests
import argparse


parser = argparse.ArgumentParser()

parser.add_argument("--url", type=str, required=True, 
                    help='sensor measurement url string')
args = parser.parse_args()
res = requests.get(args.url) 
db = SqliteDataBase()
db.PutItem(res.json())
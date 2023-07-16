from os import environ


class Config(object):
    SECRET_KEY=environ.get('FLASK_KEY') or "dupa"
    SERVER_NAME="ilenawawrze.local"
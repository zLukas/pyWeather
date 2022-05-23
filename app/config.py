from os import environ


class Config():
    SECREST_KEY=environ.get('FLASK_KEY')
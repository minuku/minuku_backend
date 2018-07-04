import os
from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('db', 27017)
db = client['minukudb']

from .core import app_setup

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)

# run those command to setup:
# docker-compose build
# docker-compose up

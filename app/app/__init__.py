from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = 'super secret string'  # Change this!
CORS(app)

db = MongoClient('db', 27017)['minukudb']

# api
from .api.user import user

app.register_blueprint(user)

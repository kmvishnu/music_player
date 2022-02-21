from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.secret_key = "user_01_key"
app.config["MONGO_URI"] = "mongodb://localhost:27017/music_user"
mongo = PyMongo(app)
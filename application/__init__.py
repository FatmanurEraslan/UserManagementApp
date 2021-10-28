from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["SECRET_KEY"] = "5baeb3390dcb6a92302abfa4c67963709bb15f56"
app.config["MONGO_URI"] = "mongodb://localhost:27017/userManagementDb"

## Setup MongoDb
mongodb_client = PyMongo(app)
db = mongodb_client.db
from application import routes
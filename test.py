import os
import secrets

from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = f"{secrets.token_urlsafe()}"
client = MongoClient(os.environ.get("MONGO_URI"))

users = client.get_default_database("users")

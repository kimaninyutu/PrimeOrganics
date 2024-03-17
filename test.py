import os
import secrets

from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = f"{secrets.token_urlsafe()}"
client = MongoClient(os.environ.get("mongodb+srv://kimanihezekiah:<password>@cluster0.atrb87s.mongodb.net/"))

users = client.users

print(users)

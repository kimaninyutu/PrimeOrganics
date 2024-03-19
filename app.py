import os
import secrets

from dotenv import load_dotenv
from flask import Flask
from pymongo import MongoClient

from routes import pages

load_dotenv()


def create_app():
    app = Flask(__name__)
    app.secret_key = f"{secrets.token_urlsafe()}"
    client = MongoClient(os.environ.get("MONGO_URI"))
    app.db = client.users  # DATABASE NAME
    users = app.db.users  # COLLECTION NAME
    app.register_blueprint(pages)
    return app

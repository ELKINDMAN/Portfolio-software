"""
    Handles imports to solve existing Circular imports issue
"""
from app_config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)

app.config['SECRET_KEY'] = 'b4fbe003b2c6b5d9ccdcbde046c7158193378db425b6822fe3c04555c0e2f326'

db = SQLAlchemy(app)

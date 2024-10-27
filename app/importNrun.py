"""
    Handles imports to solve existing Circular imports issue
"""
from app_config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
app = Flask(__name__)
app.config.from_object(Config)
mail = Mail(app)
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'b4fbe003b2c6b5d9ccdcbde046c7158193378db425b6822fe3c04555c0e2f326'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'elkanahkindness@gmail.com'
app.config['MAIL_PASSWORD']  = 'elkind2002'
app.config['MAIL_DEFAULT_SENDER'] = 'elkanahkindness@gmail.com'

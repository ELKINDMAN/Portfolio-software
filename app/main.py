'''main program logic
'''
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

#database setup
db = SQLAlchemy(app)

@app.route('/')
def landing():
    return render_template('home.html')


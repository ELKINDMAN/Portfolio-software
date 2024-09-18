"""
Model database, app instance initialization and creation
"""
from importNrun import app, db
from models import Admin, Post
with app.app_context():
    db.create_all()

    print('Database Successfully created!')

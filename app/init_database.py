"""
Model database initialization and creation
"""
from main import db, app

with app.app_context():
    db.create_all()

    print('Database Successfully created;)

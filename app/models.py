'''
Database models used for the program
'''
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from importNrun import db, app

class Admin(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=True, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    Hashed_password = db.Column(db.String(30), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def set_password(self, password):
        self.Hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.Hashed_password, password)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'), nullable=False)




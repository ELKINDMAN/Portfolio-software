'''
Database models used for the program
'''
from Python import Secrets
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from importNrun import db, app, mail
from flask_mail import Message

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
    image_urls = db.Column(db.JSON, nullable=True)
    document_urls = db.Column(db.JSON, nullable=True)

#password handling: token and reset functions
def send_token():
     return secrets.token_url_safe(32)
    
def mail_token(email, token):
    msg = Message('Password Reset Request', recipients=[email])
    msg.body = f"Your reset token is: {token}\n\nUse this to reset your password on the reset password page"
    mail.send(msg)
    

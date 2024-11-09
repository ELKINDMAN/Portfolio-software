'''
    Module that handles all mail and mailing utility
'''
import secrets
from importNrun import mail, db
from flask_mail import Message
from datetime import datetime, timedelta

def gen_token(admin):
    token = secrets.token_urlsafe(32)
    admin.reset_token = token
    admin.token_time = datetime.now() + timedelta(minutes=10)
    db.session.commit()
    return f'http://127.0.0.1:5000/reset_password/{token}'
    
def mail_token(email, url):
    msg = Message('Password Reset Request', sender="elkanahkindness@gmail.com", recipients=[email])
    msg.body = f"Your reset token is: {url}\n\nUse this to reset your password. Expires in 10 minutes"
    mail.send(msg)
    return f"Mail sent!"

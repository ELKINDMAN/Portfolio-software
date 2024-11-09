'''
    Module that handles all mail and mailing utility
'''
import secrets
from importNrun import mail
from flask_mail import Message
from datetime import datetime, timedelta

def gen_token():
    url = 'http://127.0.0.1:5000/reset_password/' + secrets.token_urlsafe(32)
    return url
    
def mail_token(email, token):
    msg = Message('Password Reset Request', sender="elkanahkindness@gmail.com", recipients=[email])
    msg.body = f"Your reset token is: {token}\n\nUse this to reset your password"
    mail.send(msg)
    return f"Mail sent!"

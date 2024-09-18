"""
simple query to view all admins
"""
from importNrun import db
from models import Admin, Post

all_admins = Admin.query.all()

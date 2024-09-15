'''main program logic
'''
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, redirect, url_for, flash, request
from models import Admin, Post
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.secret_key = 'elkindman2002p.'

login_manager = LoginManager(app)
login_manager.login_view = 'login'

# ---> home/landing page
@app.route('/')
def home():
    return render_template('home.html')

#signup
@app.route('/signup', methods=['GET', 'POST'])
def siginup():
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

#Datacheck ---->
        admin_exists = Admin.query.filter((Admin.name == name) | (Admin.email == email)).first()
        if admin_exists:
            flash('Email or Media Admin already exists!', 'danger')
            return redirect(url_for('signup'))

#Create new admin
        new_admin = Admin(name=name, username=username, email=email)
        new_admin.set_password(password)
#Adding new_admin to database
        try:
            db.session.add(new_admin)
            db.session.commit()
            flash('You have successfully become a Media Admin! Please login', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            db.session.rollback()
            flash('Error creating account. Try again.', 'danger')

    return render_template('signup.html')


#database instance
db = SQLAlchemy(app)

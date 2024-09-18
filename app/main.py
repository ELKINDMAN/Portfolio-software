'''
    main program logic
'''
#from flask_sqlalchemy import SQLAlchemy
from flask import render_template, redirect, url_for, flash, request


from models import Admin, Post
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from importNrun import db, app


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(admin_id):
    return Admin.query.get(int(admin_id))

# ---> home/landing page
@app.route('/')
def home():
    return render_template('home.html')


# ---> signup
@app.route('/signup', methods=['GET', 'POST'])
def signup():
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
            return redirect(url_for('login.html'))
        except Exception as e:
            db.session.rollback()
            flash('Error creating account. Try again.', 'danger')

    return render_template('signup.html')


# ---> login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = Admin.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user)
            flash('Logged in successfully')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'warning')

    return render_template('login.html')


# ---> dashboard
@app.route('/dashboard')
@login_required
def dashboard():
#    if current_user.is_authenticated:
    return render_template('Dashboard.html', name=current_user.name)
 #   else:
  #      return redirect(url_for('login'))



# ---> logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have logged out!')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)







from flask import render_template, redirect, url_for, flash, request
import os
from werkzeug.utils import secure_filename
from models import Admin, Post
from flask_login import login_required, current_user, LoginManager, login_user, logout_user
from importNrun import db, app


# Helper function for creating a new post with multiple images
def create_post(title, content, images, documents):
    # Check if a post with the same content already exists
    content_exists = Post.query.filter_by(content=content).first()
    if content_exists:
        flash('News article with same content already published', 'danger')
        return False
# Handle image uploads
    image_urls = []
    if images:
        for image in images:
            if image:
                image_filename = secure_filename(image.filename)
                image_path = os.path.join(app.root_path, 'static/images', image_filename)
                image.save(image_path)
                image_url = url_for('static', filename=f'images/{image_filename}')
                image_urls.append(image_url)

    # Handle document uploads
    doc_urls = []  # Corrected variable name to plural (as it should handle multiple documents)
    if documents:
        for document in documents:
            if document:
                doc_filename = secure_filename(document.filename)
                doc_path = os.path.join(app.root_path, 'static/docs', doc_filename)
                document.save(doc_path)
                doc_url = url_for('static', filename=f'docs/{doc_filename}')
                doc_urls.append(doc_url)  # Appending to the `doc_urls` list
    # Create and save new post with multiple image URLs in JSON format
    new_post = Post(title=title, content=content, image_urls=image_urls,
                    document_urls=doc_urls, admin_id=current_user.id)
    try:
        db.session.add(new_post)
        db.session.commit()
        flash('Post created successfully!', 'success')
        return True
    except Exception as e:
        db.session.rollback()
        flash('Error creating post. Try again.', 'danger')
        return False


# Helper function for deleting a post
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.admin_id != current_user.id:
        flash('You do not have the permission to delete this post', 'danger')
        return False

    try:
        db.session.delete(post)
        db.session.commit()
        flash(f'"{post.title}" has been deleted.', 'success')
        return True
    except Exception as e:
        db.session.rollback()
        flash('Error in deleting post!', 'danger')
        return False


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(admin_id):
    return Admin.query.get(int(admin_id))


# ---> home/landing page
@app.route('/')
def home():
    post = Post.query.order_by(Post.id.desc()).all()
    return render_template('home.html', post=post)


# ---> signup
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Data check
        admin_exists = Admin.query.filter((Admin.name == name) | (Admin.email == email)).first()
        if admin_exists:
            flash('Email or Media Admin already exists!', 'danger')
            return redirect(url_for('signup'))

        # Create new admin
        new_admin = Admin(name=name, username=username, email=email)
        new_admin.set_password(password)

        # Adding new admin to database
        try:
            db.session.add(new_admin)
            db.session.commit()
            flash('You have successfully become a Media Admin! Please login', 'success')
            return redirect(url_for('login'))
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
            flash('Logged in successfully', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'warning')

    return render_template('login.html')


# ---> dashboard
@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    if request.method == 'POST':
        # Handle post creation
        if 'title' in request.form and 'content' in request.form:
            title = request.form['title']
            content = request.form['content']
            images = request.files.getlist('images')  # Accept multiple image files
            documents = request.files.getlist('documents')

            if create_post(title, content, images, documents):
                return redirect(url_for('dashboard'))

        # Handle post deletion
        elif 'delete_post_id' in request.form:
            post_id = request.form['delete_post_id']
            if delete_post(post_id):
                return redirect(url_for('dashboard'))

    # If GET request, display posts and admin options (create/delete)
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('Dashboard.html', name=current_user.name, posts=posts)


@app.route('/post/<int:id>')
def news_detail(id):
    # Fetch the specific news post using the provided 'id'
    news_item = Post.query.get_or_404(id)

    # Render a template for the news detail page
    return render_template('news_detail.html', news=news_item)


# ---> logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have logged out!', 'success')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)

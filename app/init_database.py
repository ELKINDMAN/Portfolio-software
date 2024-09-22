"""
    Model database, app instance initialization and creation
"""
from importNrun import app, db
from models import Admin, Post
with app.app_context():
#    db.drop_all()
 #   print('Database dropped\ncreating new...')
    db.create_all()

    print('Database Successfully created!')

    all_admin = Admin.query.all()
    if all_admin:
        print('Admin Present in database')
        for admin in all_admin:
            print(f'Name: {admin.name},\n username: {admin.username},\n email: {admin.email}, \n password: {admin.Hashed_password}')
    posts = posts = Post.query.order_by(Post.id.desc()).all()
    if posts:
        print('Posts in database\n Latests\n')
        for post in posts:
            print(f'Headline: {post.title}\n{post.content}')

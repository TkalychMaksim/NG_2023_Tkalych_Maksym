from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

db = SQLAlchemy()
migrate = Migrate()


def create_app(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///news.db'
    db.init_app(app)
    migrate.init_app(app, db)
    return app


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    header = db.Column(db.Text, nullable=False)
    author = db.Column(db.Text, nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow())


def reg_user(user_login, user_password):
    try:
        user = Users(username=user_login, password=user_password)
        db.session.add(user)
        db.session.flush()
        db.session.commit()
    except Exception as e:
        print(e)


def login_user(user_login, user_password):
    global connect_token
    users = Users.query.all()
    for user in users:
        if user.username == user_login and user.password == user_password:
            connect_token = True
            break
        else:
            connect_token = False
    return connect_token


def post_create(header, author, post_text):
    try:
        post = Posts(header=header, author=author, text=post_text)
        db.session.add(post)
        db.session.flush()
        db.session.commit()
    except Exception as e:
        print(e)


def render_posts():
    posts = Posts.query.order_by(Posts.date.desc()).all()
    return posts


def render_post_by_id(id):
    post = Posts.query.get(id)
    return post

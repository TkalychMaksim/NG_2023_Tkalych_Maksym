from flask import Flask, redirect, render_template, request
from dbWorker import create_app, login_user, post_create, render_posts, render_post_by_id

app = Flask('WeWeNews')
app = create_app(app)


@app.route('/')
def redirect_to_posts_page():
    return redirect('/posts')


@app.route('/posts')
def render_posts_page():
    posts = render_posts()
    return render_template('posts_page.html', posts=posts)


@app.route('/posts/<int:id>')
def render_post_detail(id):
    post = render_post_by_id(id)
    return render_template('post_detail.html', post=post)


@app.route('/login')
def render_login_page():
    return render_template('login_page.html')


@app.route('/login', methods=['POST'])
def login():
    user_login = str(request.form.get('login'))
    user_password = str(request.form.get('password'))
    connect_token = login_user(user_login, user_password)
    if connect_token:
        return redirect('/editor')
    else:
        pass
    return redirect('/login')


@app.route('/editor')
def render_editor_page():
    return render_template('editor_page.html')


@app.route('/editor', methods=['POST'])
def receiving_data():
    header = request.form.get('header')
    author = request.form.get('author')
    post_text = request.form.get('post_text')
    post_create(header, author, post_text)
    return redirect('/editor')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081, debug=True)



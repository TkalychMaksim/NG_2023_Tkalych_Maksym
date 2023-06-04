from flask import Flask, render_template, request, redirect
from datetime import datetime
server = Flask("WeweChat")
users = {}
chat_messages = []


@server.route("/", methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        user_login = request.form.get('login')
        user_password = request.form.get('password')
        users[user_login] = user_password
        return redirect('/login')
    else:
        return render_template('registration_page.html')


@server.route("/login", methods=['GET', 'POST'])
def auth():
    if request.method == 'POST':
        user_login = request.form.get('login')
        user_password = request.form.get('password')
        if user_login in users and users[user_login] == user_password:
            return redirect('/chat')
        return redirect('/login')
    else:
        return render_template('login_page.html')


@server.route("/chat", methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        message = request.form.get('message')
        timestamp = datetime.now().strftime('%H:%M:%S')
        chat_messages.append((message, timestamp))
        print(chat_messages)
    return render_template('chat.html', messages=chat_messages)


server.run(host='0.0.0.0', port=8081)

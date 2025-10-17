from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = []

@app.route('/')
def home():
    return '<h1>Welcome to the Flask App</h1><a href="/login">Login</a> | <a href="/register">Register</a>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users.append({'username': username, 'password': password})
        return redirect(url_for('login'))
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import os
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Secure Secret Key
app.secret_key = os.getenv("SECRET_KEY", "change_this_in_production")


# Database Initialization
def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    conn.commit()
    conn.close()


init_db()


@app.route('/')
def home():
    return render_template('index.html')


# Register
@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        hashed_password = generate_password_hash(password)

        try:
            conn = sqlite3.connect("users.db")
            cursor = conn.cursor()

            cursor.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, hashed_password)
            )

            conn.commit()
            conn.close()

            return redirect('/login')

        except:
            return "Username already exists"

    return render_template('register.html')


# Login
@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        # Parameterized Query (Prevents SQL Injection)
        cursor.execute(
            "SELECT password FROM users WHERE username=?",
            (username,)
        )

        user = cursor.fetchone()

        conn.close()

        if user and check_password_hash(user[0], password):

            session['username'] = username

            return redirect('/dashboard')

        return "Invalid Login"

    return render_template('login.html')


# Dashboard
@app.route('/dashboard')
def dashboard():

    if 'username' not in session:
        return redirect('/login')

    return render_template(
        'dashboard.html',
        username=session['username']
    )


# Secure Search (XSS Protected by Jinja Escaping)
@app.route('/search', methods=['POST'])
def search():

    if 'username' not in session:
        return redirect('/login')

    search_term = request.form['search']

    return render_template(
        'search.html',
        search_term=search_term
    )


# Logout
@app.route('/logout')
def logout():

    session.pop('username', None)

    return redirect('/')

@app.route('/users')
def users():

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id, username, password FROM users")
    data = cursor.fetchall()

    conn.close()

    return str(data)


if __name__ == "__main__":
    app.run()
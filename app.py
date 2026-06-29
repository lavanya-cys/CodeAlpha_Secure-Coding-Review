from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "secret123"   # Hardcoded secret key (vulnerability)

# Create database and table
def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT
    )
    """)

    conn.commit()
    conn.close()

init_db()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']  # Plain text password

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO users(username,password) VALUES(?,?)",
            (username, password)
        )

        conn.commit()
        conn.close()

        return redirect('/login')

    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        # SQL Injection Vulnerability
        query = f"""
        SELECT * FROM users
        WHERE username='{username}'
        AND password='{password}'
        """

        cursor.execute(query)

        user = cursor.fetchone()

        conn.close()

        if user:
            session['user'] = username
            return redirect('/dashboard')

        return "Invalid Login"

    return render_template("login.html")


@app.route('/dashboard')
def dashboard():

    if 'user' not in session:
        return redirect('/login')

    return render_template(
        "dashboard.html",
        username=session['user']
    )


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

@app.route('/search', methods=['POST'])
def search():

    search = request.form['search']

    return f"""
    <h1>Search Results</h1>

    You searched for:

    {search}

    <br><br>

    <a href='/dashboard'>Back</a>
    """

@app.route('/users')
def users():

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()

    conn.close()

    return str(data)


if __name__ == "__main__":
    app.run(debug=True)   # Debug mode enabled (vulnerability)
@app.route('/comment', methods=['GET', 'POST'])
def comment():
    if request.method == 'POST':
        comment = request.form['comment']
        return f"Comment: {comment}"

    return '''
    <form method="POST">
        <input type="text" name="comment">
        <button type="submit">Submit</button>
    </form>
    '''

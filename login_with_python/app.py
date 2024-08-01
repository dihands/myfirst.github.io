from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database setup
def setup_database():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS forlogin (
            id TEXT PRIMARY KEY,
            passwd TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

setup_database()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        user_id = request.form['id']
        user_passwd = request.form['passwd']

        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('SELECT * FROM forlogin WHERE id=?', (user_id,))
        if c.fetchone():
            return "User ID already exists. Please choose a different ID."

        c.execute('INSERT INTO forlogin (id, passwd) VALUES (?, ?)', (user_id, user_passwd))
        conn.commit()
        conn.close()
        return redirect(url_for('home'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form['id']
        user_passwd = request.form['passwd']

        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('SELECT * FROM forlogin WHERE id=? AND passwd=?', (user_id, user_passwd))
        if c.fetchone():
            return "ri rjhf ifin eruern dfuenjfj dfoueufn eo"
        else:
            return "Invalid ID or password."
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)

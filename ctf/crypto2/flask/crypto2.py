# Cryptocraphic Failure Medium CTF created by Ibrahim Selek
# For educational purposes under Amsterdam University of Applied Sciences
from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory, session
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import sqlite3
import os

app = Flask(__name__, instance_relative_config=True)
app.config['PASSWORD_DB'] = 'passwords.db'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.secret_key = 'CTF@Challenge4@!Students724'

# Routes
@app.route('/ctf/crack-meta')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect(app.config['PASSWORD_DB'])
        c = conn.cursor()

        # Create the 'users' table if it doesn't exist
        c.execute('''CREATE TABLE IF NOT EXISTS users
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     username TEXT NOT NULL UNIQUE,
                     password TEXT NOT NULL)''')

        # Check if the username is already taken
        c.execute("SELECT * FROM users WHERE username=?", (username,))
        user = c.fetchone()
        if user:
            flash('Username already taken')
            conn.close()
            return redirect(url_for('register'))

        # Hash the password before storing it
        hashed_password = generate_password_hash(password)

        # Store the users in the database
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        conn.close()

        flash('Registration successful. Please log in.')
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect(app.config['PASSWORD_DB'])

        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=?", (username,))
        user = c.fetchone()

        if user and check_password_hash(user[2], password):
            session['username'] = username  # Store username in session
            flash('Logged in successfully.')
            return redirect(url_for('upload'))
        else:
            flash('Invalid username or password')

        conn.close()

    return render_template('login.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if 'username' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.endswith('.txt'):
            # Save the uploaded file
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            # Check if the uploaded file is a TXT file
            # If it is, redirect to the files page
            if file.content_type == 'text/plain':
                return redirect(url_for('files'))
            else:
                # Handle other file types and display an appropriate message
                flash('Uploaded file is not a TXT file')
        else:
            flash('Uploaded file is not a TXT file!')

    return render_template('upload.html')


@app.route('/files')
def files():
    if 'username' not in session:
        return redirect(url_for('login'))
    else:
        files = os.listdir(app.config['UPLOAD_FOLDER'])
        return render_template('files.html', files=files)


@app.route('/download/<filename>')
def download(filename):
    if 'username' not in session:
        return redirect(url_for('login'))
    else:
        try:
            return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)
        except FileNotFoundError:
            flash('File not found')
            return redirect(url_for('files'))




if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)


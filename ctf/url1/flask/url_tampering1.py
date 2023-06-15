from flask import Flask, render_template, redirect, url_for, flash, Blueprint, request, g, session
import mysql.connector
import os


app = Flask(__name__, instance_relative_config=True)
app.secret_key = 'CTF@Challenge4@!Students724'


@app.route('/ctf/hidden_directories')
def hidden_directories():
    return render_template('url_tampering1.html')

@app.route('/ctf/hidden_directories/secret/index.css')
def index_css():
    return render_template('hiddenwebsite/secret/index.css')

@app.route('/ctf/hidden_directories/index.html')
def home():
    return render_template('hiddenwebsite/index.html')

@app.route('/ctf/hidden_directories/about.html')
def about():
    return render_template('hiddenwebsite/about.html')

@app.route('/ctf/hidden_directories/contact.html')
def contact():
    return render_template('hiddenwebsite/contact.html')

@app.route('/ctf/hidden_directories/secret/')
def secret():
    return render_template('hiddenwebsite/secret.html')

@app.route('/ctf/hidden_directories/secret/hidden/')
def hidden():
    return render_template('hiddenwebsite/hidden.html')

@app.route('/ctf/hidden_directories/secret/hidden/superhidden/')
def superhidden():
    return render_template('hiddenwebsite/superhidden.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

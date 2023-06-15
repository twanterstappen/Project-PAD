from flask import Flask, render_template, request, flash, g, abort, abort, send_from_directory
import os


app = Flask(__name__, instance_relative_config=True)
app.secret_key = 'CTF@Challenge4@!Students724'

@app.route("/ctf/impersonation1/email-viewer")
def main():
    return render_template('home.html')

@app.route("/ctf/impersonation1/account-details")
def account():
    return render_template('account-details.html')

@app.route("/ctf/impersonation1/sent-emails")
def sent():
    return render_template('sent-emails.html')

@app.route("/ctf/impersonation1")
def description():
    return render_template('impersonation-description.html')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

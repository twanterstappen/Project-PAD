from flask import Flask, render_template
import os


app = Flask(__name__, instance_relative_config=True)
app.secret_key = 'CTF@Challenge4@!Students724'

# Cryptographic Failure Hard
@app.route('/ctf/passwordhunt')
def password_hunt():
    return render_template('crypto3.html')


@app.route('/ctf/passwordhunt/robots.txt')
def robots():
    return render_template('robots.txt')



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

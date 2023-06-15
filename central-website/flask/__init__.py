from flask import Flask, render_template, redirect, url_for, flash, Blueprint, request, g, session, abort
import os
import datetime
import mysql.connector
import auth
import user
import view
import ctf
import error
import db

config = db.get_db()




app = Flask(__name__, instance_relative_config=True)
app.secret_key = 'CTF@Challenge4@!Students724'

app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(days=31)
app.config['SESSION_COOKIE_SAMESITE'] = None


app.register_blueprint(auth.bp)
app.register_blueprint(user.bp)
app.register_blueprint(view.bp)
app.register_blueprint(ctf.bp)
app.register_blueprint(error.bp)





if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

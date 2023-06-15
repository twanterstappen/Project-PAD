from flask import Flask, render_template, redirect, url_for, flash, Blueprint, request, g, session, abort, app
import mysql.connector
import bcrypt
import db
config = db.get_db()
bp = Blueprint('auth', __name__)


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if 'email' in session:
        return redirect(url_for('home'))
    if request.method == 'POST':
        try:
            # retrieve the form, password needs to be in bits(utf-8)
            firstname = request.form['firstname']
            prefix = request.form['prefix']
            lastname = request.form['lastname']
            nickname = request.form['nickname']
            email = request.form['email']
            password = request.form['password'].encode('utf-8')
            # hash and salt password
            password_h = bcrypt.hashpw(password, bcrypt.gensalt())
            # Check if prefix is empty
            if prefix == '':
                prefix = None
            # check if the required forms are filled in
            if '' in (firstname, lastname, email, nickname, password):
                flash('Please fill in the required fields!', 'error')
                return render_template('register.html')
            # Check if the password contains a valid password
            password = str(password)
            if len(password) < 8 or not any(c.isupper() for c in password) or not any(c.islower() for c in password) or not any(c.isdigit() for c in password):
                message = "Password must contain at least 8 characters, including at least one uppercase letter, one lowercase letter, and one digit"
                return render_template('register.html', message=message)
           

            # Check if email is already in use
            connect = mysql.connector.connect(**config)
            cursor = connect.cursor()

            query = "SELECT email FROM user WHERE email = %s; SELECT nickname FROM user WHERE nickname = %s;"
            param = (email, nickname)

            email_nickname = []
            for result in cursor.execute(query, param, multi=True):
                entry = result.fetchone()
                if entry:
                    for e in entry:
                        email_nickname.append(e)
                        entry = None


            if email_nickname:
                if nickname in email_nickname and email in email_nickname:
                    flash('Nickname and Email already used', 'error')
                elif email in email_nickname:
                    flash('Email already used', 'error')
                else:
                    flash('Nickname already used', 'error')
                   
                return render_template('register.html')

            # Adding user in database
            query = "INSERT INTO user VALUES (NULL, %s, %s, %s, %s, %s, %s);"
            param = (firstname, prefix, lastname, email, nickname, password_h)
            cursor.execute(query, param)
            connect.commit()
            connect.close
            flash('Successfully registered', 'success')
            return redirect(url_for('auth.login'))
        except:
            abort(503, 'Database')
    return render_template('register.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if 'email' in session:
        return redirect(url_for('home'))
    if request.method == 'POST':
        
        email = request.form['email']
        password = request.form['password'].encode('utf-8')
            # connect
        try:
            connect = mysql.connector.connect(**config)
            cursor = connect.cursor()
            query = "SELECT id, password, nickname from user where email = %s;"
            param = (email, )
            cursor.execute(query, param)
            entry = cursor.fetchone()
            connect.close
            if entry and bcrypt.checkpw(password, entry[1].encode('utf-8')):
                try:
                    if request.form.getlist('remember')[0] == 'remembermonth':
                        session.permanent = True
                except:
                    session.permanent = False
                session['email'] = email
                session['user_id'] = entry[0]
                flash(f"Welcome { entry[2] }, you succussfully logged in!", "success")
                return redirect(url_for('ctf.ctf'))
            else:
                flash('Email and/or password wrong', 'error')

        except:
            abort(503, 'Database')
    return render_template('login.html')

@bp.route('/logout')
def logout():
    session.clear()
    flash("You've been logged out", 'info')
    return redirect(url_for('view.home'))

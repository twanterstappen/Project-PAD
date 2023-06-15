from flask import Flask, render_template, redirect, url_for, flash, Blueprint, request, g, session, abort, app
import mysql.connector
import bcrypt
import db
config = db.get_db()
bp = Blueprint('user', __name__)


@bp.route('/profile', methods=('GET', 'POST'))
def profile():
    if 'email' not in session:
        return redirect(url_for('auth.login'))
    
    email = session['email']
    user_id = session['user_id']

    # Connect to the database
    connect = mysql.connector.connect(**config)
    cursor = connect.cursor()
    
    # Retrieve user information from the database
    query = "SELECT firstname, prefix, lastname, nickname, email, password FROM user WHERE id = %s;"
    param = (user_id, )
    cursor.execute(query, param)
    user = cursor.fetchone()

    # Retrieve entries from ctf_favourite table for the user
    query = """select * from ctf_favourite where user_id = %s;""" 
    param = (user_id, )
    cursor.execute(query, param)
    entry_1 = cursor.fetchall()
    g.entry_1 = entry_1
    
    # Close the database connection
    connect.close()
    

    if request.method == 'POST':
        save = 0
        unsave = 0
        try:
            save = request.form['save']
        except:
            None
        try:
            unsave = request.form['unsave']
        except:
            None           
        try:
            if save:
                connect = mysql.connector.connect(**config)
                cursor = connect.cursor()
                query = "INSERT INTO user.favourite VALUES(%s, %s);"
                param = (save, user_id)
                cursor.execute(query, param)
                connect.commit()
                connect.close
                return redirect(url_for('user.profile'))
            elif unsave:
                connect = mysql.connector.connect(**config)
                cursor = connect.cursor()
                query = "DELETE FROM user.favourite WHERE ctf_id = %s and user_id = %s;"
                param = (unsave, user_id)
                cursor.execute(query, param)
                connect.commit()
                connect.close
                return redirect(url_for('user.profile'))
        except:
            flash('Could not save or delete to/from favourite', 'error')

        like = 0
        unlike = 0
        remove = 0
        change_like = 0
        change_unlike = 0
        try:
            like = request.form['like']
        except:
            None
        try:
            unlike = request.form['unlike']
        except:
            None           
        try:
            change_like = request.form['change_like']
        except:
            None           
        try:
            change_unlike = request.form['change_unlike']
        except:
            None           
        try:
            remove = request.form['remove']
        except:
            None           
        try:
            if like:
                connect = mysql.connector.connect(**config)
                cursor = connect.cursor()
                query = "INSERT INTO user.like_unlike VALUES(%s, %s, 1);"
                param = (like, user_id)
                cursor.execute(query, param)
                connect.commit()
                connect.close
                return redirect(url_for('user.profile'))
            elif unlike:
                connect = mysql.connector.connect(**config)
                cursor = connect.cursor()
                query = "INSERT INTO user.like_unlike VALUES(%s, %s, 0);"
                param = (unlike, user_id)
                cursor.execute(query, param)
                connect.commit()
                connect.close
                return redirect(url_for('user.profile'))
            elif change_like:
                connect = mysql.connector.connect(**config)
                cursor = connect.cursor()
                query = "UPDATE user.like_unlike SET like_unlike.like = 1 WHERE ctf_id = %s and user_id = %s;"
                param = (change_like, user_id)
                cursor.execute(query, param)
                connect.commit()
                connect.close
                return redirect(url_for('user.profile'))
            elif change_unlike:
                connect = mysql.connector.connect(**config)
                cursor = connect.cursor()
                query = "UPDATE user.like_unlike SET like_unlike.like = 0 WHERE ctf_id = %s and user_id = %s;"
                param = (change_unlike, user_id)
                cursor.execute(query, param)
                connect.commit()
                connect.close
                return redirect(url_for('user.profile'))
            elif remove:
                connect = mysql.connector.connect(**config)
                cursor = connect.cursor()
                query = "DELETE FROM user.like_unlike WHERE ctf_id = %s and user_id = %s;"
                param = (remove, user_id)
                cursor.execute(query, param)
                connect.commit()
                connect.close
                return redirect(url_for('user.profile'))
        except:
            flash('Could not add or delete to/from favourite', 'error')
        connect.close

        # Process the form data if a POST request is made
        firstname = request.form['firstname']
        prefix = request.form['prefix']
        lastname = request.form['lastname']
        new_email = request.form['email']
        nickname = request.form['nickname']

        if prefix == '':
            prefix = None
        
            
        if '' in (firstname, lastname, new_email, nickname):
            flash('Please fill the required fields!', 'error')
            return render_template('profile.html', user=user)
        
        # Connect to the database again        
        connect = mysql.connector.connect(**config)
        cursor = connect.cursor()
        
        # Check if the new email and nickname are already used by other users
        query = "SELECT email FROM user WHERE email = %s; SELECT nickname FROM user WHERE nickname = %s;"
        param = (new_email, nickname)

        email_nickname = []
        for result in cursor.execute(query, param, multi=True):
            entry = result.fetchone()
            if entry:
                for e in entry:
                    email_nickname.append(e)
                    entry = None
        
        # Check if the new email and nickname are already used by other users
        if email_nickname:
            if nickname in email_nickname and nickname != user[3] and new_email in email_nickname and new_email != user[4]:
                flash('Nickname and Email already used', 'error')
                return redirect(url_for('user.profile'))
            elif nickname in email_nickname and nickname != user[3]:
                flash('Nickname already used', 'error')
                return redirect(url_for('user.profile'))
            elif new_email in email_nickname and new_email != user[4]:
                flash('Email already used', 'error')
                return redirect(url_for('user.profile'))

        # Update the user's profile in the database
        update_query = """
            UPDATE user SET 
            firstname=%s, 
            prefix=%s, 
            lastname=%s, 
            email=%s,
            nickname=%s 
            WHERE id=%s;
        """
        update_params = (firstname, prefix, lastname, new_email, nickname, user_id)
        cursor.execute(update_query, update_params)
        connect.commit()
        connect.close()
        flash('Profile was successfully updated', 'success') 
    
        return redirect(url_for('user.profile'))
   
   # Render the profile page with the user's information
    return render_template('profile.html', user=user)


@bp.route('/leaderbord')
def leaderbord():
    if 'email' not in session:
        return redirect('auth.login')
    user_id = session['user_id']
    connect = mysql.connector.connect(**config)
    cursor = connect.cursor()
    query = """SELECT nickname, total_points, position FROM user_scoreboard ORDER BY position ASC LIMIT 10"""
    cursor.execute(query)
    entry_1 = cursor.fetchall()
    g.entry_1 = entry_1
    query = """SELECT nickname, total_points, position FROM user_scoreboard WHERE user_id = %s"""
    param = (user_id,)
    cursor.execute(query, param)
    user_points = cursor.fetchone()
    g.user_points = user_points
    connect.close
    return render_template('leaderbord.html')


@bp.route('/completed', methods=('GET', 'POST'))
def completed():
    if 'email' not in session:
        return redirect(url_for('auth.login'))
    email = session['email']
    user_id = session['user_id']


    if request.method == 'POST':
        save = 0
        unsave = 0
        try:
            save = request.form['save']
        except:
            None
        try:
            unsave = request.form['unsave']
        except:
            None           
        try:
            if save:
                connect = mysql.connector.connect(**config)
                cursor = connect.cursor()
                query = "INSERT INTO user.favourite VALUES(%s, %s);"
                param = (save, user_id)
                cursor.execute(query, param)
                connect.commit()
                connect.close
                return redirect(url_for('user.completed'))
            elif unsave:
                connect = mysql.connector.connect(**config)
                cursor = connect.cursor()
                query = "DELETE FROM user.favourite WHERE ctf_id = %s and user_id = %s;"
                param = (unsave, user_id)
                cursor.execute(query, param)
                connect.commit()
                connect.close
                return redirect(url_for('user.completed'))
        except:
            flash('Could not save or delete to/from favourite', 'error')

        like = 0
        unlike = 0
        remove = 0
        change_like = 0
        change_unlike = 0
        try:
            like = request.form['like']
        except:
            None
        try:
            unlike = request.form['unlike']
        except:
            None           
        try:
            change_like = request.form['change_like']
        except:
            None           
        try:
            change_unlike = request.form['change_unlike']
        except:
            None           
        try:
            remove = request.form['remove']
        except:
            None           
        try:
            if like:
                connect = mysql.connector.connect(**config)
                cursor = connect.cursor()
                query = "INSERT INTO user.like_unlike VALUES(%s, %s, 1);"
                param = (like, user_id)
                cursor.execute(query, param)
                connect.commit()
                connect.close
                return redirect(url_for('user.completed'))
            elif unlike:
                connect = mysql.connector.connect(**config)
                cursor = connect.cursor()
                query = "INSERT INTO user.like_unlike VALUES(%s, %s, 0);"
                param = (unlike, user_id)
                cursor.execute(query, param)
                connect.commit()
                connect.close
                return redirect(url_for('user.completed'))
            elif change_like:
                connect = mysql.connector.connect(**config)
                cursor = connect.cursor()
                query = "UPDATE user.like_unlike SET like_unlike.like = 1 WHERE ctf_id = %s and user_id = %s;"
                param = (change_like, user_id)
                cursor.execute(query, param)
                connect.commit()
                connect.close
                return redirect(url_for('user.completed'))
            elif change_unlike:
                connect = mysql.connector.connect(**config)
                cursor = connect.cursor()
                query = "UPDATE user.like_unlike SET like_unlike.like = 0 WHERE ctf_id = %s and user_id = %s;"
                param = (change_unlike, user_id)
                cursor.execute(query, param)
                connect.commit()
                connect.close
                return redirect(url_for('user.completed'))
            elif remove:
                connect = mysql.connector.connect(**config)
                cursor = connect.cursor()
                query = "DELETE FROM user.like_unlike WHERE ctf_id = %s and user_id = %s;"
                param = (remove, user_id)
                cursor.execute(query, param)
                connect.commit()
                connect.close
                return redirect(url_for('user.completed'))
        except:
            flash('Could not like or unlike', 'error')

        connect.close



    connect = mysql.connector.connect(**config)
    cursor = connect.cursor()
    query = """select * from ctf_complete where user_id = %s;"""
    param = (user_id,)
    cursor.execute(query, param)
    entry = cursor.fetchall()
    entry_1 = entry
    g.entry_1 = entry_1
    connect.close
            

    return render_template('complete.html')

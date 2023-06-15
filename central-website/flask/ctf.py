from flask import Flask, render_template, redirect, url_for, flash, Blueprint, request, g, abort, session
import os
import mysql.connector
import db
config = db.get_db()

bp = Blueprint('ctf', __name__)


@bp.route('/submit-flag', methods=('GET', 'POST'))
def submitflag():
    if 'email' in session:
        if request.method == 'POST':
            flag = request.form['flag']
            email = session['email']
            user_id = session['user_id']
            # connect
            try:
                connect = mysql.connector.connect(**config)
                cursor = connect.cursor()
                query = "SELECT flag.ctf_id, ctf.ctf from flag JOIN user.ctf ON flag.ctf_id = ctf.id where flag = %s;"
                param = (flag, )
                cursor.execute(query, param)
                entry = cursor.fetchone()
                
                if entry:
                    ctf_id = entry[0]
                    ctf_name = entry[1]
                    g.level_name = ctf_name

                    query = "SELECT * FROM complete WHERE ctf_id = %s AND user_id = %s;"
                    param = (ctf_id, user_id)
                    cursor.execute(query, param)
                    entry = cursor.fetchone()
                    if not entry:
                        query = "INSERT INTO complete VALUES (%s, %s);"
                        param = (ctf_id, user_id)
                        cursor.execute(query, param)
                        connect.commit()
                    else:
                        flash(f'You already solved level {ctf_name}', 'info')
                else:
                    flash(f'Submitted flag is wrong', 'error')
                connect.close
            except:
                abort(400, f'You tried to submit flag {flag}')
        return render_template('submit-flag.html')
    return redirect(url_for('auth.login'))
            


@bp.route('/ctf', methods=('GET', 'POST'))
def ctf():
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
            elif unsave:
                connect = mysql.connector.connect(**config)
                cursor = connect.cursor()
                query = "DELETE FROM user.favourite WHERE ctf_id = %s and user_id = %s;"
                param = (unsave, user_id)
                cursor.execute(query, param)
                connect.commit()
                connect.close
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
            elif unlike:
                connect = mysql.connector.connect(**config)
                cursor = connect.cursor()
                query = "INSERT INTO user.like_unlike VALUES(%s, %s, 0);"
                param = (unlike, user_id)
                cursor.execute(query, param)
                connect.commit()
                connect.close
            elif change_like:
                connect = mysql.connector.connect(**config)
                cursor = connect.cursor()
                query = "UPDATE user.like_unlike SET like_unlike.like = 1 WHERE ctf_id = %s and user_id = %s;"
                param = (change_like, user_id)
                cursor.execute(query, param)
                connect.commit()
                connect.close
            elif change_unlike:
                connect = mysql.connector.connect(**config)
                cursor = connect.cursor()
                query = "UPDATE user.like_unlike SET like_unlike.like = 0 WHERE ctf_id = %s and user_id = %s;"
                param = (change_unlike, user_id)
                cursor.execute(query, param)
                connect.commit()
                connect.close
            elif remove:
                connect = mysql.connector.connect(**config)
                cursor = connect.cursor()
                query = "DELETE FROM user.like_unlike WHERE ctf_id = %s and user_id = %s;"
                param = (remove, user_id)
                cursor.execute(query, param)
                connect.commit()
                connect.close
        except:
            flash('Could not save or delete to/from favourite', 'error')
            

    sort_challenge = request.args.get('sort_challenge')
    if sort_challenge == '' or sort_challenge == None:
        sort_challenge = '%'
    if sort_challenge == '%':
        g.sort_challenge = ''
    else:
        g.sort_challenge = sort_challenge

    difficulty_challenge = request.args.get('difficulty_challenge')
    if difficulty_challenge == '' or difficulty_challenge == None:
        difficulty_challenge = '%'
    if difficulty_challenge == '%':
        g.difficulty_challenge = ''
    else:
        g.difficulty_challenge = difficulty_challenge



    try:
        # connect
        connect = mysql.connector.connect(**config)
        cursor = connect.cursor()
        query = """SELECT * FROM ctf_view WHERE user_id = %s and sort like %s and difficulty like %s"""
        param = (user_id, sort_challenge, difficulty_challenge)
        cursor.execute(query, param)
        entry = cursor.fetchall()
        entry_1 = entry


        query = "SELECT ctf_id, COUNT(user_id) AS user_count FROM complete GROUP BY ctf_id ORDER BY user_count DESC LIMIT 1;"
        cursor.execute(query, )
        entry = cursor.fetchone()
        try:
            g.h_ctf = entry[0]
        except:
            None

        query = "select sort from ctf GROUP BY sort;"
        cursor.execute(query,)
        entry = cursor.fetchall()
        entry_2 = entry
        connect.close

        query = "select difficulty from ctf GROUP BY difficulty;"
        cursor.execute(query,)
        entry = cursor.fetchall()
        entry_3 = entry
        connect.close
    

        g.entry_1 = entry_1
        g.entry_2 = entry_2
        g.entry_3 = entry_3
    except:
        abort(503, 'Database')
    return render_template('ctf.html')
    

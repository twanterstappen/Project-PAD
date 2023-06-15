from flask import Flask, render_template, redirect, url_for, flash, Blueprint, request, g, session, abort, app
import mysql.connector
import bcrypt
import db
config = db.get_db()
bp = Blueprint('view', __name__)


@bp.route('/')
def home():
    try:    # Try to execute the code within this block
        
        # Connect to the database
        connect = mysql.connector.connect(**config)
        cursor = connect.cursor()
        
        # Retrieve the ctf_id with the highest user_count from the 'complete' table 
        query = "SELECT ctf_id, COUNT(user_id) AS user_count FROM complete GROUP BY ctf_id ORDER BY user_count DESC LIMIT 1;"
        cursor.execute(query, )
        entry = cursor.fetchone()
        ctf_id = entry[0]

        # Retrieve the ctf and sort information based on the ctf_id 
        query = "select ctf, sort from ctf where id = %s;"
        param = (ctf_id, )
        cursor.execute(query, param)
        entry = cursor.fetchone()
        connect.close
        g.m_lvl = entry
    except: # If an exception occurs during the try block, control flows to this block
        None
    return render_template('home.html')

@bp.route('/how-to-play')
def howtoplay():
    return render_template('how-to-play.html')

@bp.route('/about-us')
def aboutus():
    return render_template('about-us.html')

@bp.route('/learn')
def learn():
    return render_template('learn.html')

@bp.route('/contact')
def contract():
    return render_template('contact.html')

@bp.route('/terms-of-service')
def termsofserivce():
    return render_template('terms-of-service.html')
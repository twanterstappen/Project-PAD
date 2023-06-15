from flask import Flask, render_template, request, flash, g, abort, abort, Blueprint
import mysql.connector
import os


bp = Blueprint('phpmyadmin', __name__,  static_folder='templates/phpmyadmin', static_url_path='', url_prefix='/ctf')



@bp.route('/phpmyadmin', methods=('GET', 'POST'))
def test():
    if request.method != 'POST':
        flash('Please login first!', 'info')
    if request.method == 'POST':
        # Request information from the form
        name = request.form['name']
        password = request.form['password']
        try:
            connect = mysql.connector.connect(host="dbsql1",port=3308,database="sql1",user="sql1",password="Hello@CTF546!")
            cursor = connect.cursor()
            # query that will allow sql injection, but only the data name and password from user
            query = f"SELECT name, password from user where name = '{name}' and password = '{password}';"
            cursor.execute(query, multi=False)
            entry = cursor.fetchall()
            connect.close
            if entry:
                if ';' not in name and ';' not in password and 'union' not in name.lower() and 'union' not in password.lower() and 'select' not in name.lower() and 'select' not in password.lower():
                    g.entry = entry
                    return render_template('flag.html')
                else:
                    flash('Do not use ; (semicolon), select and/or union', 'warning')
            elif ';' in name or ';' in password or 'union' in name.lower() or 'union' in password.lower() or 'select' in name.lower() or 'select' in password.lower():
                flash('Do not use ; (semicolon), select and/or union', 'warning')
            else:
                flash('Name and/or Password wrong', 'warning')
            
        except:
            flash(f'You tried to submit Name: " {name} ", Password: " {password} ". Currently unable to handle this request!', 'error')
    return render_template('phpmyadmin/phpmyadmin.html')


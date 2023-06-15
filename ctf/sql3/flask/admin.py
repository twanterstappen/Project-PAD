from flask import render_template, request, g, Blueprint
import mysql.connector

# Create a blueprint for the 'admin' module
bp = Blueprint('admin', __name__, static_folder='templates/wordpress', static_url_path='', url_prefix='/ctf/wordpress')

# Route for the WordPress admin login
@bp.route('/wp-admin', methods=('GET', 'POST'))
def wordpress():
    if request.method != 'POST':
        g.message = 'Please login first!'
    
    if request.method == 'POST':
        # Retrieve the entered name and password from the form
        name = request.form['name']
        password = request.form['password']

        try:
            # Connect to the MySQL database
            connect = mysql.connector.connect(host="dbsql3", port=3310, database="sql3", user="sql3", password="Hello@CTF546!")
            cursor = connect.cursor()

            # Query to check if the entered name and password match the user table
            query = f"SELECT name, password FROM user WHERE name = '{name}' AND password = '{password}';"
            
            col = []
            # Execute the query and retrieve the columns and entries
            for result in cursor.execute(query, multi=True):
                columns = cursor.description
                entry_1 = result.fetchall()
            # ave the column name into a list
            if columns:
                for column in columns:
                    col.append(column[0])

            # Query to retrieve the names and passwords from the superuser table
            query = f"SELECT name, password FROM superuser;"
            cursor.execute(query, multi=False)
            entry_2 = cursor.fetchall()
            
            counter = 0
            # Check if the entered name and password match the superuser credentials
            for i in entry_2:
                if name == i[0] and password == i[1]:
                    counter += 1
            
            g.flag = None
            if counter > 0:
                g.flag = 'CyberCTF{What$about#that@injection?}'

            # Close connection
            connect.close()
            
            # dissallow the show command
            if 'show' in name.lower() or 'show' in password.lower():
                g.message = "Don't use show!"
                return render_template('wordpress/wp-login.html')
            # if there is an entry or someone logged in with superuser account
            elif entry_1 or g.flag:
                g.len = len(entry_1)
                g.entry = entry_1
                g.col = col
                g.range = range(len(g.col))
                return render_template('logged.html')
        
            else:
                g.message = 'Name and/or Password wrong!'            
        except:
            g.message = 'Error 500, database'

    return render_template('wordpress/wp-login.html')

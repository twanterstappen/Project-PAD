from flask import Flask, render_template, flash, request, g
import mysql.connector
import os
import base64

# Create Flask app
app = Flask(__name__, instance_relative_config=True)

# Set secret key for session management
app.secret_key = 'CTF@Challenge4@!Students724'

# SQL Injection medium
@app.route('/ctf/vaccine4you', methods=('GET', 'POST'))
def sql2():
    if request.method == 'POST':
        try:
            # Get the name and password from the form data
            name = request.form['name']
            password_f = request.form['password']

            # Encode the password using base64
            message_bytes = password_f.encode('ascii')
            base64_bytes = base64.b64encode(message_bytes)
            password = base64_bytes.decode('ascii')

            # Connect to the MySQL database
            connect = mysql.connector.connect(host="dbsql2", port=3309, database="sql2", user="sql2", password="Hello@CTF546!")
            
            # Create a cursor object to execute SQL queries
            cursor = connect.cursor()

            # Construct the SQL query with user input
            query = f"SELECT name, vaccine FROM user WHERE name = '{name}' AND password = '{password}';"

            # Execute the SQL query
            for result in cursor.execute(query, multi=True):
                entry = result.fetchone()

            # Close the database connection
            connect.close

            # If an entry is found, store it in the global g object and render the logged-in template
            if entry:
                g.entry = entry
                return render_template('logged-in.html')
            else:
                flash('Name and/or Password wrong', 'warning')
        except:
            # If an exception occurs, display an error message
            flash(f'You tried to submit Name: " {name} ", Password: " {password_f} " to database `user`. Currently unable to handle this request!', 'error')

    # Render the login template for GET requests and unsuccessful login attempts
    return render_template('login.html')


# Catch remaining errors
@app.errorhandler(Exception)
def general(error):
    error_code = str(error)
    error_code = error_code[:3]
    if error_code == '404':
        g.path = request.path

    g.error = error
    return render_template("error/general.html")

if __name__ == '__main__':
    # Get the port from the environment variable, or use the default port 5000
    port = int(os.environ.get('PORT', 5000))
    # Run the Flask app
    app.run(debug=True, host='0.0.0.0', port=port)

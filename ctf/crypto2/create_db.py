import sqlite3
# Script to create user database
def create_user_database():
    conn = sqlite3.connect('flask/passwords.db')
    c = conn.cursor()

    # Creating users table
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 username TEXT NOT NULL,
                 password TEXT NOT NULL)''')

    conn.commit()
    conn.close()

# Create the user database if it doesn't exist
create_user_database()

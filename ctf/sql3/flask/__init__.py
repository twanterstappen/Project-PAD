# Import necessary modules
from flask import Flask, render_template, request, g
import os
import wordpress
import admin

# Create a Flask application instance
app = Flask(__name__, instance_relative_config=True)

# Set the secret key for the application
app.secret_key = 'CTF@Challenge4@!Students724'

# Register the 'wordpress' blueprint
app.register_blueprint(wordpress.bp)

# Register the 'admin' blueprint
app.register_blueprint(admin.bp)

# Catch remaining errors
@app.errorhandler(Exception)
def general(error):
    # Extract the error code from the exception
    error_code = str(error)
    error_code = error_code[:3]
    
    # If it's a 404 error, store the requested path in the global 'g' object
    if error_code == '404':
        g.path = request.path
    
    # Store the error itself in the global 'g' object
    g.error = error
    
    # Render the 'general.html' template to display the error
    return render_template("error/general.html")

# Run the Flask application
if __name__ == '__main__':
    # Get the port number from the environment variables or use the default value 5000
    port = int(os.environ.get('PORT', 5000))
    
    # Run the Flask application with debug mode enabled, allowing access from any IP address
    app.run(debug=True, host='0.0.0.0', port=port)

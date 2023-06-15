from flask import Flask, render_template, request, flash, g, abort, abort, send_from_directory
import os
import phpmyadmin

app = Flask(__name__, instance_relative_config=True)
app.secret_key = 'CTF@Challenge4@!Students724'
app.register_blueprint(phpmyadmin.bp)


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
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

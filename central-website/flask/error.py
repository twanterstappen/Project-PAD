from flask import Flask, render_template, redirect, url_for, flash, Blueprint, request, g

bp = Blueprint('error', __name__)

# Catch remaining errors
@bp.app_errorhandler(Exception)
def general(error):
    error_code = str(error)
    error_code = error_code[:3]
    if error_code == '404':
        g.path = request.path
        
    g.error = error
    
    return render_template("error/general.html")
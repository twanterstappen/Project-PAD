from flask import render_template, Blueprint



bp = Blueprint('wordpress', __name__,  static_folder='templates/wordpress', static_url_path='', url_prefix='/ctf')



@bp.route('/wordpress', methods=('GET', 'POST'))
def home():
    return render_template('wordpress/sample-page/index.html')




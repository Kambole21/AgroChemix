from flask import Blueprint, render_template

bp = Blueprint('about_us', __name__)

@bp.route('/about-us')
def about_page():
    return render_template('about_us.html')
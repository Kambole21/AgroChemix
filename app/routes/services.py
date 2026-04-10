from flask import Blueprint, render_template

bp = Blueprint('services', __name__)

@bp.route('/services')
def services_page():
    return render_template('services/services.html')
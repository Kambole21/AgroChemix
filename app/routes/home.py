from flask import Blueprint, render_template
from app import app

bp = Blueprint('home', __name__)

@bp.route('/')
@bp.route('/Agro-Home')
def home_page():
    return render_template('home.html')

@bp.route('/google5dbdfa7605fe07f1.html')
def googole_verify():
    return app.send_static_file('google5dbdfa7605fe07f1.html')
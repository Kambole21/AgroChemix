from flask import Blueprint, render_template

bp = Blueprint('products', __name__)

@bp.route('/products')
def products_page():
    return render_template('products/products.html')
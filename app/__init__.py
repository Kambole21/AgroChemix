from flask import Flask
import os

app = Flask(__name__, template_folder="templates")

app.config['SECRET_KEY'] = '3fde2ba708cb1315091272ef6bdd6ac3'

app.config['SENDGRID_API_KEY'] = os.getenv('SENDGRID_API_KEY')
app.config['MAIL_DEFAULT_SENDER'] = 'andrew.mulenga@agrochemix.info'
app.config['MAIL_RECIPIENT'] = 'andrew.mulenga@agrochemix.info'

# Register blueprints
from app.routes import home, about_us, services, contact, products
app.register_blueprint(home.bp)
app.register_blueprint(about_us.bp)
app.register_blueprint(services.bp)
app.register_blueprint(contact.bp)
app.register_blueprint(products.bp)

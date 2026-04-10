from flask import Flask
from flask_mail import Mail
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__, template_folder="templates")

# Set configurations
app.config['SECRET_KEY'] = '3fde2ba708cb1315091272ef6bdd6ac3'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587  # Use integer directly
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'andrew.mulenga@agrochemix.info'
app.config['MAIL_PASSWORD'] = 'khwz tvkb gefa ojdg'
app.config['MAIL_DEFAULT_SENDER'] = 'andrew.mulenga@agrochemix.info'
app.config['MAIL_RECIPIENT'] = 'andrew.mulenga@agrochemix.info'

# Initialize mail AFTER all config is set
mail = Mail(app)  # Pass app directly instead of using init_app

# Store mail in extensions for access in blueprints
app.extensions['mail'] = mail

# Register blueprints
from app.routes import home, about_us, services, contact, products
app.register_blueprint(home.bp)
app.register_blueprint(about_us.bp)
app.register_blueprint(services.bp)
app.register_blueprint(contact.bp)
app.register_blueprint(products.bp)
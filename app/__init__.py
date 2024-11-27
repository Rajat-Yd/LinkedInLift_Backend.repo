from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from config import Config

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Load configurations from Config class

    # Initialize extensions with the app
    db.init_app(app)
    migrate.init_app(app, db)

    # Initialize Flask-Admin
    admin = Admin(app, name='Admin Panel', template_mode='bootstrap3')

    # Register your models with Flask-Admin
    from app.models import ContactMessage  # Ensure this import is correct
    admin.add_view(ModelView(ContactMessage, db.session))

    # Register blueprints
    from app.routes import main  # Import blueprint after initializing extensions
    app.register_blueprint(main)

    return app

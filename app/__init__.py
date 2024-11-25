from flask import Flask
from .routes import main

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)
    app.config['SECRET_KEY'] = '220225012@rajoihskj'
    return app

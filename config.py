import os

class Config:
    SECRET_KEY = os.urandom(24)
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'instance/site.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Suppress deprecation warnings

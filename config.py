import os

class Config:
    SECRET_KEY = os.urandom(24)
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'instance/site.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Suppress deprecation warnings
    MAIL_SERVER = 'smtp.gmail.com'  # Using Gmail's SMTP server
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'rajat0911q@gmail.com'  # Replace with your email
    MAIL_PASSWORD = 'jeoo ofga nxdt tyok'  # Replace with your email password
    MAIL_DEFAULT_SENDER = 'rajat0911q@gmail.com'
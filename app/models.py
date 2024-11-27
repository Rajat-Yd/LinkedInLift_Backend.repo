from app import db

class ContactMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Auto-incrementing ID
    name = db.Column(db.String(100), nullable=False)  # Name of the user
    email = db.Column(db.String(120), unique=False, nullable=False)  # Email of the user
    message = db.Column(db.Text, nullable=False)  # Message content
    phone = db.Column(db.Integer, unique=False, nullable=False)  # Phone content
    linkedin = db.Column(db.String(120), unique=False, nullable=False)  # LinkedIn content
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)  # Timestamp

    def __repr__(self):
        return f"ContactMessage('{self.name}', '{self.email}', '{self.timestamp}', '{self.phone}', '{self.linkedin}')"

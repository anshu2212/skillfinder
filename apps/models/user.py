from sqlalchemy.sql import func
from .db import db



# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(20), unique=True, nullable=False)  # Assuming a maximum length for phone numbers
    password = db.Column(db.String(20), default=None)
    status = db.Column(db.String(20), default='Created')
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now(), nullable=False)
    
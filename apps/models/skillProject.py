from sqlalchemy.sql import func
from .db import db


# User model
class SkillProject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    skill_id = db.Column(db.Integer, nullable=False)
    source = db.Column(db.String(20), default='Upworks')
    price = db.Column(db.String(20), default=None)
    project_at = db.Column(db.DateTime(timezone=True), nullable=False)
    project_type = db.Column(db.String(20),default='Hourly')
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now(), nullable=False)

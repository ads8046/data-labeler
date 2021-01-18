from app.base import db


class UserPhotoLabel(db.Model):
    photo_id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False)
    user_selection = db.Column(db.Boolean)
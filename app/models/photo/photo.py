from app.base import db


class Photo(db.Model):
    photo_id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False)
    photo_name = db.Column(db.String(255), nullable=False)
    photo_date = db.Column(db.DateTime)

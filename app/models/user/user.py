from app.base import db


class User(db.Model):
    user_id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email_address = db.Column(db.String(100), nullable=False)

    def get_user(user_id):
        return user_id

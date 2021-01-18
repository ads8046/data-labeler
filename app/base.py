from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
import datetime
import requests

import os

app = Flask(__name__, template_folder='views/templates', static_folder='views/static')
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "photodatabase.db"))
app.config['SQLALCHEMY_DATABASE_URI'] = database_file

db = SQLAlchemy(app)


class Photos(db.Model):
    photo_id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False)
    photo_name = db.Column(db.String(255), nullable=False)
    photo_date = db.Column(db.DateTime)

    def __repr__(self):
        return "<Title: {}>".format(self.title)


class User(db.Model):
    user_id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email_address = db.Column(db.String(100), nullable=False)


class UserPhotoSwipes(db.Model):
    photo_id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False)
    user_selection = db.Column(db.Boolean)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

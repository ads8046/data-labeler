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


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

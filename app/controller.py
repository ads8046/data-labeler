from app.base import app
from flask import render_template, url_for,request, redirect
import string, re
from flask_sqlalchemy import SQLAlchemy


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials! Please try again.'
        else:
            return redirect(url_for('index.html'))
    return render_template('auth/login.html', error=error)


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    invalid_chars = set(string.punctuation.replace("-", ""))
    email_regex = "[A-Za-z0-9-_]+(.[A-Za-z0-9-_]+)*@[A-Za-z0-9-]+(.[A-Za-z0-9]+)*(.[A-Za-z]{2,})+"

    if request.method == 'POST':
        name_input_str = request.form.get("name")
        email_input_str = request.form.get("email")

        # full name check
        if any(char in invalid_chars for char in name_input_str):
            error = 'Invalid Full Name. Only upper-case letters, lower-case letters and hyphens("-") are allowed.'

        # email address check
        elif request.form['email'] == 'email in db' or ( re.match(email_regex, email_input_str) is False ):
            error = 'There already exists an account registered under this email address.'

        #password check

        else:
            return redirect(url_for('index.html'))
    return render_template('auth/register.html', error=error)
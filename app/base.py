from flask import Flask, render_template, url_for
import requests

app = Flask(__name__, template_folder='views/templates', static_folder='views/static')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

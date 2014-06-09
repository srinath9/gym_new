# from flask import Flask
# from flask import render_template
# from app import app

# @app.route('/')
# @app.route('/index')
# @app.route('/events')

from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def api_root():
    return 'Welcome'

@app.route('/articles')
def articles():
    return 'List of ' + url_for('articles')

@app.route('/articles/<articleid>')
def article(articleid):
    return 'You are reading ' + articleid

@app.route('/random-number/<int:number>')
def random_number(number):
  # If the user browsed /hello/John, the output would be
  # "Hello John!"
    return 'Number %d!' % number

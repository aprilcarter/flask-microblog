from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'april'}
    posts = [
        {
            'author': {'username': 'Piglet'},
            'body': 'Beautiful day in Portland'
        },
        {
            'author': {'username': 'Tigger'},
            'body': 'The Avengers movie was so cool'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

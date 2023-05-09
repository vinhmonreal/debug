from . import bp
from flask import render_template

@bp.route('/')
def home():
    matrix = {
        'instructors': ('Dr. Chuck', 'Charles Severance'),
        'students': ['Rex', 'Ryan', 'Randy', 'Ralph']
    }
    return render_template('index.jinja', title = 'Home', instructors = matrix['instructors'], students = matrix['students'])

@bp.route('/about')
def about():
    return render_template('about.jinja', title = 'About')

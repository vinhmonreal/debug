from flask import render_template, flash, redirect, url_for
from .models import User
from . import bp
from app.forms import RegisterForm

@bp.route('/register', methods = ['GET', 'POST'])
def register():
    forms = RegisterForm()
    if forms.validate_on_submit():
        username = forms.username.data
        user = User.query.filter_by(username = username).first()
        email = User.query.filter_by(email = forms.email.data).first()
        if not user and not email:
            user = User(username = forms.username.data, email = forms.email.data, password = forms.password.data)
            user.commit()
            flash(f'Account created for {username}!', 'success')
            return redirect(url_for('main.index'))
        elif user:
            flash(f'User {username} already exists!')
        else:
            flash(f'Email {email} already exists!')
    return render_template('register.jinja', title = 'Register', form = forms)

@bp.route('/signin')
def signin():
    return render_template('signin.jinja', title = 'Sign In')
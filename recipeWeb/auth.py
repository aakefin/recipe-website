from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/login_page', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home_page'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login_page.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        password1 = request.form.get('password')
        password2 = request.form.get('confirm_password')
        print('hi11')
        user = User.query.filter_by(email=email).first()
        print('hi122')
        if user:
            flash('Email already exists.', category='error')
            print('hi122')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
            print('hi12333')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
            print('hi122444')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
            print('hi12255')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
            print('hi12266')
        else:
            print('h2313777')
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home_page'))

    return render_template("signup_page.html", user=current_user)
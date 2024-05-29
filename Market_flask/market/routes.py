from . import app
from flask import render_template, redirect, url_for, flash
from .forms import RegisterForm, LoginForm
from .models import User
from . import db
from flask_login import login_user, logout_user, login_required


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/market')
@login_required
def market_page():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]
    users = User.query.all()
    user_list = [{"id": user.id, "name": user.username, 'email': user.email_address} for user in users]
    return render_template("market.html", items=items, users=user_list)


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f'Account "{user_to_create.username}" created successfully!', category='success')
        return redirect(url_for("market_page"))
    if form.errors != {}:  # If there are no errors from validation
        for error in form.errors.keys():
            flash(f"Validation error: {error}", category='danger')
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if (attempted_user is not None) and attempted_user.check_password_correction(
                attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f'Successfully loged in as {attempted_user.username}!', category='success')
            return redirect(url_for('market_page'))
        else:
            flash("Username and password are not match!", category='danger')

    return render_template('login.html', form=form)


@app.route('/logout_page')
def logout_page():
    logout_user()
    flash(f"You have been successfully log out!", category='info')
    return redirect(url_for('home_page'))

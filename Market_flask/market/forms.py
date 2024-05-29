from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from .models import User
from flask import flash


class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()  # user.query always gives object
        if user is not None:
            flash(f"DB error: Username exists", category='danger')
            raise ValidationError("Username already exists in db! try different one")

    def validate_email(self, email_to_check):
        user = User.query.filter_by(email_address=email_to_check.data).first()  # user.query always gives object
        if user is not None:
            flash(f"DB error: Email exists", category='danger')
            raise ValidationError("Email already exists in db! try different one")

    username = StringField(label='User Name: ', validators=[DataRequired(), Length(min=3, max=30)])
    email = EmailField(label='Email: ', validators=[DataRequired(), Email()])
    password1 = PasswordField(label='Password: ', validators=[DataRequired(), Length(min=4)])
    password2 = PasswordField(label='Confirm Password: ', validators=[DataRequired(), EqualTo("password1")])
    submit = SubmitField(label='Create account')


class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')

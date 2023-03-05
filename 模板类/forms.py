from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField


class RegistrationForm(FlaskForm):
    # The name of the field is the name of the variable
    username = StringField('Username')
    email = StringField('Email')
    password = PasswordField('Password')
    confirm_password = PasswordField('Confirm Password')
    submit = SubmitField('Sign Up')
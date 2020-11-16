from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(message="Email is required"), Length(1, 64), Email(message="Not a valid email")])
    password = PasswordField('Password', validators=[DataRequired(message="Password is required")])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')
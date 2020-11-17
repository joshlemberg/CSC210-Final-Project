from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import ValidationError
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from ..models import User

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(message="Email is required"), Length(1, 64), Email(message="Not a valid email")])
    password = PasswordField('Password', validators=[DataRequired(message="Password is required")])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')

class SignUpForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(message="Email is required"), Length(1, 64), Email(message="Not a valid email")])
    username = StringField('Username', validators=[DataRequired(message="Username is required"), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, message="Username must have only letters, numbers, dots, or underscores.")])
    # We should change the regexp for whatever we want it to be for Username
    password = PasswordField('Password', validators=[DataRequired(message="Password is required"), EqualTo('passwordConfirm', message="Passwords must match")])
    passwordConfirm = PasswordField('Confirm Password', validators=[DataRequired("Password Confirmation is required")])
    submit = SubmitField('Sign Up')

    '''
    Page 116:
    This form also has two custom validators implemented as methods. 
    When a form defines a method with the prefix 'validate_' followed by the name of a field, the method is invoked in addition to any regularly defined validators. 
    In this case, the custom validators for email and username ensure that the values given are not duplicates. 
    The custom validators indicate a validation error by raising a ValidationError exception with the text of the error message as an argument.
    '''
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('That email is already registered to an account.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('That username has already been taken.')




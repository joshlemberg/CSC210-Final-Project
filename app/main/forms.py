from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms import ValidationError
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from ..models import User

class GliderForm(FlaskForm):
	body = TextAreaField("What do you think?", validators=[DataRequired()])
	submit = SubmitField('Submit')

class FishForm(FlaskForm):
	body = TextAreaField("What do you think?", validators=[DataRequired()])
	submit = SubmitField('Submit')

class LadylogForm(FlaskForm):
	body = TextAreaField("What do you think?", validators=[DataRequired()])
	submit = SubmitField('Submit')


class NoseriderForm(FlaskForm):
	body = TextAreaField("What do you think?", validators=[DataRequired()])
	submit = SubmitField('Submit')
	
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
# from flask_mail import Mail
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = "if you're reading this it's too late"
# app.config['MAIL_SERVER'] = 'smtp.googlemail.com' 
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USE_TLS'] = True 
# app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME') 
# app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
application = app
bootstrap = Bootstrap(app)
moment = Moment(app)
# mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')

class Role(db.Model):
	__tablename__ = 'roles'
	id = db.Column(db.Integer, primary_key=True) 
	name = db.Column(db.String(64), unique=True)
	def __repr__(self):
		return '<Role %r>' % self.name

from werkzeug.security import generate_password_hash, check_password_hash
class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), unique=True, index=True)
	password_hash = db.Column(db.String(128))

	@property
	def password(self):
		raise AttributeError('Password is not a readable attribute')

	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)
	
	def __repr__(self):
		return '<User %r>' % self.username

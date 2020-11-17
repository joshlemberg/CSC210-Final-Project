# Put the database models in here
# FIXME not sure what to import
from . import db, login_manager
from flask import current_app

class Role(db.Model):
	__tablename__ = 'roles'
	id = db.Column(db.Integer, primary_key=True) 
	name = db.Column(db.String(64), unique=True)
	def __repr__(self):
		return '<Role %r>' % self.name

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

class User(UserMixin, db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(64), unique=True, index = True)
	username = db.Column(db.String(64), unique=True, index=True)
	password_hash = db.Column(db.String(128))
	role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
	confirmed = db.Column(db.Boolean, default=False) # Has the account been confirmed by email?

	@property
	def password(self):
		raise AttributeError('Password is not a readable attribute')

	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)

	def generate_confirmation_token(self, expiration=3600):
		s = Serializer(current_app.config['SECRET_KEY'], expiration) # Constructor for TimedJSONWebSignatureSerializer that takes an encryption key and an expiration time (in seconds) as arguments
		return s.dumps({'confirm': self.id}).decode('utf-8') # dumps method generates a cryptographic signature for the data given as an argument and then serializes the data plus the signature as a convenient token string

	def confirm(self, token):
		s = Serializer(current_app.config['SECRET_KEY'])
		try:
			data = s.loads(token.encode('utf-8')) # Try to decode the token. Raises an error if signature or expiration are invalid
		except: 
			return False
		if data.get('confirm') != self.id: # If the wrong user is being confirmed, don't confirm them
			return False
		self.confirmed = True
		db.session.add(self)
		return True

	def __repr__(self):
		return '<User %r>' % self.username



""" 
This decorator is used  to register the function with Flask-Login, which will call it when it 
needs to retrieve information about the logged-in user.
"""
@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))
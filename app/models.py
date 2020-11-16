# Put the database models in here
# FIXME not sure what to import
from . import db, login_manager

class Role(db.Model):
	__tablename__ = 'roles'
	id = db.Column(db.Integer, primary_key=True) 
	name = db.Column(db.String(64), unique=True)
	def __repr__(self):
		return '<Role %r>' % self.name

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(64), unique=True, index = True)
	username = db.Column(db.String(64), unique=True, index=True)
	password_hash = db.Column(db.String(128))
	role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

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


""" 
This decorator is used  to register the function with Flask-Login, which will call it when it 
needs to retrieve information about the logged-in user.
"""
@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))
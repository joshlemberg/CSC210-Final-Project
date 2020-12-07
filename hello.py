# from flask import Flask, render_template
# from flask_bootstrap import Bootstrap
# from flask_moment import Moment
# from flask_sqlalchemy import SQLAlchemy
# # from flask_mail import Mail
import os
from app.models import User, Role
from app import create_app, db
from flask import Flask, request, url_for, redirect, render_template

app = create_app(os.getenv('FLASK_CONFIG') or 'default') 

@app.shell_context_processor
def make_shell_context():
	return dict(db=db, User=User, Role=Role)

@app.cli.command() 
def test():
	"""Run the unit tests."""
	import unittest
	tests = unittest.TestLoader().discover('tests') 
	unittest.TextTestRunner(verbosity=2).run(tests)

# @app.route('/ladylog')
# def ladylog():
# 	return render_template('ladylog.html')

# @app.route('/fish')
# def fish():
# 	return render_template('fish.html')

# @app.route('/glider')
# def glider():
# 	return render_template('glider.html')

# @app.route('/noserider')
# def noserider():
# 	return render_template('noserider.html')

# basedir = os.path.abspath(os.path.dirname(__file__))

# app = Flask(__name__)
# app.config['SECRET_KEY'] = "if you're reading this it's too late"
# # app.config['MAIL_SERVER'] = 'smtp.googlemail.com' 
# # app.config['MAIL_PORT'] = 587
# # app.config['MAIL_USE_TLS'] = True 
# # app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME') 
# # app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
# application = app
# bootstrap = Bootstrap(app)
# moment = Moment(app)
# # mail = Mail(app)

from flask import render_template, session, redirect, url_for
from . import main
from flask_login import login_required
# from ..models import [names of models]

@main.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')

@main.route('/secret')
@login_required
def secret():
	return 'Only authenticated users are allowed!!'
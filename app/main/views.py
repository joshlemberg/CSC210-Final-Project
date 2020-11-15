from flask import render_template, session, redirect, url_for
from . import main
# from ..models import [names of models]

@main.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')
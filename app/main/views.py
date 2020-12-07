from flask import render_template, session, redirect, url_for, request, flash
from . import main
from flask_login import login_user, logout_user, current_user, login_required
from .forms import GliderForm, LadylogForm, FishForm, NoseriderForm
from ..models import Glider, Ladylog, Fish, Noserider
from .. import db
# from ..models import [names of models]

@main.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')

@main.route('/secret')
@login_required
def secret():
	return 'Only authenticated users are allowed!!'

### LADYLOG CODE
@main.route('/ladylog', methods=['GET', 'POST'])
@login_required
def ladylog():
	form = LadylogForm()
	if form.validate_on_submit():
		review = Ladylog(review=form.body.data, author=current_user._get_current_object())
		db.session.add(review)
		db.session.commit()
		return redirect(url_for('main.ladylog'))
	reviews = Ladylog.query.order_by(Ladylog.timestamp.desc()).all()
	return render_template('ladylog.html', form=form, reviews=reviews)

# This function redirects from the LadyLog review page, and allows the user to edit their comment
@main.route('/ladylogedit/<int:reviewid>', methods=['GET', 'POST'])
@login_required
def ladylogedit(reviewid):
	oldreview = Ladylog.query.get_or_404(reviewid)
	form = LadylogForm()
	if request.method == 'POST' and form.is_submitted() and form.validate():
		body = request.form.get('body')
		newreview = Ladylog(review=body, author=oldreview.author, timestamp=oldreview.timestamp)
		db.session.add(newreview)
		db.session.delete(oldreview)
		db.session.commit()
		flash("Successfully Edited Review")
	else: # Error handling referenced from https://stackoverflow.com/questions/6463035/wtforms-getting-the-errors
		for errorField, errorMessages in form.errors.items():
			for err in errorMessages:
				flash(err)
	return redirect(url_for('main.ladylog'))

# This function redirects from the LadyLog review page, and allows the user to delete their comment
@main.route('/ladylogdelete/<int:reviewid>', methods=['GET', 'POST'])
@login_required
def ladylogdelete(reviewid):
	oldreview = Ladylog.query.get_or_404(reviewid)
	db.session.delete(oldreview)
	db.session.commit()
	flash("Successfully Removed Review")
	return redirect(url_for('main.ladylog'))


### FISH CODE
@main.route('/fish', methods=['GET', 'POST'])
@login_required
def fish():
	form = FishForm()
	if form.validate_on_submit():
		review = Fish(review=form.body.data, author=current_user._get_current_object())
		db.session.add(review)
		db.session.commit()
		return redirect(url_for('main.fish'))
	reviews = Fish.query.order_by(Fish.timestamp.desc()).all()
	return render_template('fish.html', form=form, reviews=reviews)

# This function redirects from the Fish review page, and allows the user to edit their comment
@main.route('/fishedit/<int:reviewid>', methods=['GET', 'POST'])
@login_required
def fishedit(reviewid):
	oldreview = Fish.query.get_or_404(reviewid)
	form = FishForm()
	if request.method == 'POST' and form.is_submitted() and form.validate():
		body = request.form.get('body')
		newreview = Fish(review=body, author=oldreview.author, timestamp=oldreview.timestamp)
		db.session.add(newreview)
		db.session.delete(oldreview)
		db.session.commit()
		flash("Successfully Edited Review")
	else: # Error handling referenced from https://stackoverflow.com/questions/6463035/wtforms-getting-the-errors
		for errorField, errorMessages in form.errors.items():
			for err in errorMessages:
				flash(err)
	return redirect(url_for('main.fish'))

# This function redirects from the Fish review page, and allows the user to delete their comment
@main.route('/fishdelete/<int:reviewid>', methods=['GET', 'POST'])
@login_required
def fishdelete(reviewid):
	oldreview = Fish.query.get_or_404(reviewid)
	db.session.delete(oldreview)
	db.session.commit()
	flash("Successfully Removed Review")
	return redirect(url_for('main.fish'))


### GLIDER CODE
@main.route('/glider', methods=['GET', 'POST'])
@login_required
def glider():
	form = GliderForm()
	if form.validate_on_submit():
		review = Glider(review=form.body.data, author=current_user._get_current_object())
		db.session.add(review)
		db.session.commit()
		return redirect(url_for('main.glider'))
	reviews = Glider.query.order_by(Glider.timestamp.desc()).all()
	return render_template('glider.html', form=form, reviews=reviews)
	
# This function redirects from the Glider review page, and allows the user to edit their comment
@main.route('/glideredit/<int:reviewid>', methods=['GET', 'POST'])
@login_required
def glideredit(reviewid):
	oldreview = Glider.query.get_or_404(reviewid)
	form = GliderForm()
	if request.method == 'POST' and form.is_submitted() and form.validate():
		body = request.form.get('body')
		newreview = Glider(review=body, author=oldreview.author, timestamp=oldreview.timestamp)
		db.session.add(newreview)
		db.session.delete(oldreview)
		db.session.commit()
		flash("Successfully Edited Review")
	else: # Error handling referenced from https://stackoverflow.com/questions/6463035/wtforms-getting-the-errors
		for errorField, errorMessages in form.errors.items():
			for err in errorMessages:
				flash(err)
	return redirect(url_for('main.glider'))

# This function redirects from the Glider review page, and allows the user to delete their comment
@main.route('/gliderdelete/<int:reviewid>', methods=['GET', 'POST'])
@login_required
def gliderdelete(reviewid):
	oldreview = Glider.query.get_or_404(reviewid)
	db.session.delete(oldreview)
	db.session.commit()
	flash("Successfully Removed Review")
	return redirect(url_for('main.glider'))


### NOSERIDER CODE
@main.route('/noserider', methods=['GET', 'POST'])
@login_required
def noserider():
	form = NoseriderForm()
	if form.validate_on_submit():
		review = Noserider(review=form.body.data, author=current_user._get_current_object())
		db.session.add(review)
		db.session.commit()
		return redirect(url_for('main.noserider'))
	reviews = Noserider.query.order_by(Noserider.timestamp.desc()).all()
	return render_template('noserider.html', form=form, reviews=reviews)

# This function redirects from the Noserider review page, and allows the user to edit their comment
@main.route('/noserideredit/<int:reviewid>', methods=['GET', 'POST'])
@login_required
def noserideredit(reviewid):
	oldreview = Noserider.query.get_or_404(reviewid)
	form = NoseriderForm()
	if request.method == 'POST' and form.is_submitted() and form.validate():
		body = request.form.get('body')
		newreview = Noserider(review=body, author=oldreview.author, timestamp=oldreview.timestamp)
		db.session.add(newreview)
		db.session.delete(oldreview)
		db.session.commit()
		flash("Successfully Edited Review")
	else: # Error handling referenced from https://stackoverflow.com/questions/6463035/wtforms-getting-the-errors
		for errorField, errorMessages in form.errors.items():
			for err in errorMessages:
				flash(err)
	return redirect(url_for('main.noserider'))

# This function redirects from the Noserider review page, and allows the user to delete their comment
@main.route('/noseriderdelete/<int:reviewid>', methods=['GET', 'POST'])
@login_required
def noseriderdelete(reviewid):
	oldreview = Noserider.query.get_or_404(reviewid)
	db.session.delete(oldreview)
	db.session.commit()
	flash("Successfully Removed Review")
	return redirect(url_for('main.noserider'))
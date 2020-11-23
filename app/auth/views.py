from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from . import auth
from ..models import User
from .forms import LoginForm, SignUpForm, ChangePasswordForm, ChangeUsernameForm
from .. import db
from ..email import send_email

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data) # Logs in user and remembers them if they want
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.index')
            return redirect(next)
        flash('Invalid username or password')
    return render_template('auth/login.html', form=form)

@auth.route('/logout')
def logout():
    logout_user()
    flash('You have been successfully logged out.')
    return redirect(url_for('main.index'))

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        token = user.generate_confirmation_token()
        send_email(user.email, 'Confirm Your Account', 'auth/email/confirm', user=user, token=token)
        flash('You have been signed up! A confirmation email has been sent to you.')
        return redirect(url_for('auth.login'))
    return render_template('auth/signup.html', form=form)

@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('main.index'))
    if current_user.confirm(token): # Calls on confirm(self, token) from User in models.py
        db.session.commit()
        flash('Your account has been confirmed!')
    else:
        flash('The account confirmation link is invalid or has expired.')
    return redirect(url_for('main.index'))


@auth.route('/confirm')
@login_required
def resend_confirmation():
    token = current_user.generate_confirmation_token()
    send_email(current_user.email, 'Confirm Your Account', 'auth/email/confirm', user=current_user, token=token)
    flash('A new confirmation email has been sent to you.')
    return redirect(url_for('main.index'))

@auth.route('/profile')
@login_required
def profile():
    return render_template('auth/profile.html')

@auth.route('/deleteaccount')
@login_required
def delete_account():
    user = User.query.filter_by(username=current_user.username).first()
    db.session.delete(user)
    db.session.commit()
    flash('Your account has been deleted.')
    return redirect(url_for('main.index'))

@auth.route('/changepassword', methods=['GET', 'POST'])
@login_required
def change_password():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        if current_user.verify_password(form.oldPassword.data):
            current_user.password = form.newPassword.data
            db.session.add(current_user)
            db.session.commit()
            flash('Your password has been changed.')
            return render_template('auth/profile.html')
        else:
            flash('Your "Old Password" was incorrect.')
    return render_template("auth/change_password.html", form=form)


@auth.route('/changeusername', methods=['GET', 'POST'])
@login_required
def change_username():
    form = ChangeUsernameForm()
    if form.validate_on_submit():
        if current_user.verify_password(form.password.data):
            current_user.username = form.newUsername.data
            db.session.add(current_user)
            db.session.commit()
            flash('Your username has been changed.')
            return render_template('auth/profile.html')
        else:
            flash('Your password was incorrect.')
    return render_template("auth/change_username.html", form=form)
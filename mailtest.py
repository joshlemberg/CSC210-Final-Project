def main(app):
	from flask_mail import Message
	from hello import mail
	msg = Message('hahaha I sent this from flask', sender='lembergjosh@gmail.com', recipients=['jlemberg@u.rochester.edu'])
	msg.body = 'haha i sent this from flask through the terminal'
	msg.html = 'This is the <b>HTML</b> body'
	with app.app_context():
		mail.send(msg)
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
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
application = app
bootstrap = Bootstrap(app)
moment = Moment(app)
# mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')
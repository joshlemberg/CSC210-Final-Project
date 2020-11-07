from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = "if you're reading this it's too late"
application = app
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')
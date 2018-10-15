from flask import Flask, render_template 
app = Flask(__name__)
from app import app

from app.forms import LoginForm

@app.route('/login')
def login():
	form = LoginForm()
	return render_template('login.html', title = 'Sign In', form = form)
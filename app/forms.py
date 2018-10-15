from flask_wtf import Flaskform
from wtforms import StrigField, PasswordField, SubmitField
from wtforms.validators import Datarequired

class LoginForm(Flaskform):
	username = StrigField('username', validators = [Datarequired()])
	password = PasswordField('Password', validators = [Datarequired()])
	remember_me = BooleanField('Remember Me')
	submit = SubmitField('Sign In')
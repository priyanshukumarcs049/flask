# coding: utf-8
from flask import Flask

app = Flask(__name__)
@app.route('/Priyanshu')
def hello_world():
	return 	'My name is Priyanshu kumar'
@app.route('/address/')
def address():
	return 'Sri baswa Joyti Nilayam, Madhapur, Hyderabad'

@app.route('/Priyanshu/<name>')
def variable(name):
	return "hello %s!" % name	

@app.route('/flat/<int:flatno>')
def flat_no(flatno):
	return "Your Flat NO is %d." %flatno

@app.route('/rev/<float:revNo>')
def revision(revNo):
   return 'Revision Number %f' % revNo

@app.route('/flask')
def hello_flask():
   return 'Hello Flask'

@app.route('/python/')
def hello_python():
   return 'Hello Python'   

# app.add_url_rule('/', 'addres', address)	
if __name__ == '__main__':
	app.run(port = 8008, debug = True)	

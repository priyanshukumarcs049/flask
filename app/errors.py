from flask import Flask, redirect, url_for, render_template, request, abort 
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('student.html')

@app.route('/login', methods = ['POST', 'GET'])
def login():
	if request.methods == 'POST':
		if request.form ['username'] == 'admin' :
			return redirect(url_for('success'))
		else:
			abort(401)
	else:			
		return redirect(url_for('index'))

@app.route('/success')
def success():
	return 'Logged in successfully'

if __name__ == '__main__':
	app.run(port = 7001, debug = True)	
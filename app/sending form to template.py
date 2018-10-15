from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def student():
	return render_template('student.html')

@app.route('/result', method = ['POST', 'GET'])
def result():
	if request.method == 'POST'
	result = request.form
	return render_template("result2.html", result = result)

if __name__ == '__main__':
	app.run(port = 6003, debug = True)	
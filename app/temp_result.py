from flask import Flask, render_template
app = Flask(__name__)

@app.route('/result')
def result():
	dict = {'math':95, 'physics':67, 'chem': 70}
	return render_template('result.html', result = dict)

if __name__ == '__main__':
	app.run(port = 5005, debug = True)

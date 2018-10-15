from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Priyanshukumar'}
	posts = [
		{
			'author':{'username':'Priyanshu'},
			'body': 'beautiful day in hyderabad!'
		},
		{
			'author':{'username': 'Rummy'},
			'body':'gangs of wasyepur was a nice moive!'
		}
	]
	return render_template('index.html', title = 'Home', user = user,posts = posts)

if __name__ == '__main__':
	app.run(port = 7008, debug = True)
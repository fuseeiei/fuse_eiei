from flask import Flask, render_template, jsonify, request
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html',title='home')

@app.route('/hello/<name>')
def hello_name(name):
    return render_template('hello.html',title='hello_name',name=name)

@app.route('/upload', methods =['POST'])
def upload():
	return "Success"
	
@app.route('/pingpong', methods =['POST']) 
def pingpong():
	data = request.form.get('text')
	if data == 'ping':
		return "pong"
	else:
		return data
if __name__ == '__main__':
    app.run(debug=True)

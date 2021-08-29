import flask
from random import sample
from string import ascii_letters,digits
from base64 import b64decode
app = flask.Flask("Content uploader")
image = None
@app.route('/')
def index():
	return """
	<h1>Content uploader</h1>
	This is server side image uploader<br>
	plz don't abuse<br>
	i beg<br>
	Usage is post picture data (body of response)<br>
	return is random string bitch<br>
	upload anything you want<br>
	don\'t fucking expect server to open your bitchass file
	<a href=\"/downloadclient\">client download my client side content uploader y e s</a>
	
	"""
@app.route('/save',methods=['POST'])
def save():
	image = b64decode(flask.request.data)
	string = ''.join(sample(ascii_letters+digits,10)) + flask.request.headers.get("extension")
	a = open("stuff/" + string,"wb")
	a.write(image)
	a.close()
	return string ,202
@app.route('/downloadclient',methods=['GET'])
def client():
	return flask.send_file("client.py",as_attachment=True)
@app.route('/<pic>')
def get(pic):
	try:
		a = flask.send_file("stuff/" + pic)
	except Exception as e:
		return str(e)
	else:
		return a
@app.route('/favicon.ico')
def favicon():
	return flask.send_from_directory(".","favicon.ico")
app.run('0.0.0.0',80)
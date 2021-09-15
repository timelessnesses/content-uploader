from random import sample
from string import ascii_letters,digits
from base64 import b64decode
from json import load,dump

import flask

def write(ip:str,file:str):
	with open("list.json","r") as i:
		ips = load(i)
		if ip not in list(ips):
			ips[ip] = []
		ips[ip].append(file)
	with open("list.json","w") as i:
		dump(ips,i)
		return True

app = flask.Flask("Content uploader")

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
	<a href=\"/downloadclient\">client download my client side content uploader</a>
	<br>no violent or porn upload to server plz
	<br> this is alternative storage plz don't put such a heavy file
	"""
	write(flask.request.remote_addr,"GET index.html")
@app.route('/save',methods=['POST'])
def save():
	image = flask.request.data
	string = ''.join(sample(ascii_letters+digits,10)) + flask.request.headers.get("extension")
	a = open("stuff/" + string,"wb")
	a.write(image)
	a.close()
	write(flask.request.environ["REMOTE_ADDR"],f"POST {string}")
	return string ,202
@app.route('/downloadclient',methods=['GET'])
def client():
	write(flask.request.remote_addr,"GET client.py")
	return flask.send_file("client.py",as_attachment=True)
@app.route('/<pic>')
def get(pic):
	if pic == "yes.osk":
		return flask.send_file("stuff/yes.osz")
	try:
		print(flask.request.args.get("preview"))
		a = flask.send_file("stuff/" + pic,as_attachment=True if flask.request.args.get("preview") is not None or flask.request.args.get("preview") == "false" else False)
		write(flask.request.environ["REMOTE_ADDR"],f"GET {pic} FILE ")
	except Exception as e:
		return "No files found you idiot"
	else:
		return a
@app.route('/favicon.ico')
def favicon():
	return flask.send_from_directory(".","favicon.ico")
if __name__ == '__main__':
	app.run('0.0.0.0',80)

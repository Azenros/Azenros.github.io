from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)

@app.route("/hello", methods =['GET'])
def hello():
	value = request.args.get("namevar")
	return render_template("hello.html", name = value)

@app.route("/hack")
def hack():
	return "2nd Route established. Good work"	

@app.route("/login")
def login():
	return render_template("login.html")

@app.route("/login2", methods=['POST'])
def login2():
	user = request.form["username"]
	pw = request.form["password"]
	print("user logged in with: " + user + pw)
	return "yeetlmao"

app.run()
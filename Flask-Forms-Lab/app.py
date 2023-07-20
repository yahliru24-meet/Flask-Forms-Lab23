from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)
app.config['SECRET_KEY'] = 'super-secret-key'

accounts = {"yahli": ["R123", ["Gilad","Sam","Guy", "Daniela", "Costa", "Tom"]], "Said": ["Said", ["Gilad","Sam"]] , "Yazan": ["YZ", ["Costa", "Tom"]]}
# facebook_friends=["Gilad","Sam","Guy", "Daniela", "Costa", "Tom"]


@app.route('/',  methods=['GET', 'POST'])  # '/' for the default page
def login():
	if request.method == "GET":
		return render_template('login.html')
	else:
		global input_usr
		input_usr = request.form['username']
		input_pswrd = request.form['password']
		if (input_usr in accounts.keys()) and (input_pswrd == accounts[input_usr][0]):
			return redirect(url_for('home'))
		else:
			return render_template("login.html")


@app.route('/home', methods=['GET', 'POST'])
def home():
	return render_template("home.html", friends = accounts[input_usr][1])


@app.route("/friend_exists/<string:name>")
def friend_exists(name):
	return render_template("friend_exists.html", name = name, friends = accounts[input_usr][1])


if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)
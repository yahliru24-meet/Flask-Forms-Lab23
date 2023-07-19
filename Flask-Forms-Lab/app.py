from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)
app.config['SECRET_KEY'] = 'super-secret-key'

username = "yahli"
password = "123"
facebook_friends=["Gilad","Sam","Guy", "Daniela", "Costa", "Tom"]


@app.route('/',  methods=['GET', 'POST'])  # '/' for the default page
def login():
	if request.method == "GET":
		return render_template('login.html')
	else:
		input_usr = request.form['username']
		input_pswrd = request.form['password']
		if (input_usr == username) and (input_pswrd == password):
			return redirect(url_for('home'))
		else:
			return render_template("login.html")


@app.route('/home', methods=['GET', 'POST'])
def home():
	return render_template("home.html", friends = facebook_friends)


@app.route("/friend_exists/<string:name>")
def friend_exists(name):
	return render_template("friend_exists.html", name = name, friends = facebook_friends)


if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)
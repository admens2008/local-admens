from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

def create_app():
	app = Flask(__name__)
	app.config['SECRET_KEY'] = 'helloworld'

	@app.route("/")
	def home():
		return "<h1>Good Evening Gowah</h1>"
	
	@app.route("/profile")
	def profile():
		return "<h1>Gowah is a Software Engineer</h1>"

	return app
#OS
import os

# Webapp
from flask import Flask
from webBP import webBP

PORT = os.environ.get("PORT")

app = Flask(__name__)

if __name__ == "__main__":
	
	app.register_blueprint(webBP)
	app.run("0.0.0.0",PORT,debug=False)

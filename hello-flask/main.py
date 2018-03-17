from flask import Flask # this imports the Flask class from the flask module.

app = Flask(__name__) # app will be the object created by the constructor Flask. 

app.config['DEBUG'] = True #  the DEBUG configuration setting for the Flask application will be enabled. 

@app.route("/")
def index():
    return "Hello World in Flaskish"

app.run() 
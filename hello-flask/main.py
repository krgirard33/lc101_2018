from flask import Flask

app = Flask(__name__) 
app.config['DEBUG'] = True

@app.route("/")
def index():
    ''' Hello World '''
    return "Hello World in Flaskish"

app.run()

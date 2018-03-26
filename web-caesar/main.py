from flask import Flask, request # this imports the Flask class from the flask module.
import cgi
from caesar import rotate_string


app = Flask(__name__) # app will be the object created by the constructor Flask. 

app.config['DEBUG'] = True #  the DEBUG configuration setting for the Flask application will be enabled. 

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <!-- create your form here -->
      <form action='/' method='POST'>
        <label>Rotate by:
              <input name="rot" type="text" value="0" />
              <textarea name="text" type="text" placeholer="Place message here">{0}</textarea>
        </label>
        <input type="submit" />
      </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format('')

@app.route("/", methods = ['POST'])
def encrypt():
    rot = int(request.form['rot'])

    e_mess = ""
    for character in request.form['text']:
        e_mess += rotate_string(character, rot)
        e_mess=cgi.escape(e_mess)
    return form.format(e_mess)


app.run()


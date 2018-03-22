from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = '''
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <!-- create your form here -->
      <label>Rotate by:
          <input name="rot" type="text" value="0" />
          <input name="text" type="text" />
      </label>
      <input type="submit" />
      
    </body>
</html>
'''

@app.route("/", methods = ['POST'])
def index():
    return form 

@app.route("/", methods = ['POST'])
def ecrypt(rot, text):
    rot = int(rot)
    text = text
    e_mess = ""
    for character in text:
        e_mess += rotate_string(character, rot)
    return "<h1>{e_mess}</h1>"


app.run()


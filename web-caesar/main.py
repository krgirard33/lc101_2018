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
      <form>
      <label>Rotate by:
          <input id="rot" name="rot" type="text" value="0" />
          <textarea name="text" type="text" placeholder="Enter message here...">{0}</textarea>
      </label>
      <input type="submit" />
      </form>
      
    </body>
</html>
'''

@app.route("/", methods = ['POST'])
def index():
    return form.format('') 

@app.route("/", methods = ['POST'])
def ecrypt(rot, text):
    rot = int(request.form['rot'])
    text = request.form['text']
    e_mess = rotate_string(rot, text)
    return form.formated(e_mess)
    


app.run()


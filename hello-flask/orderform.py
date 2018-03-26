from flask import Flask, request # this imports the Flask class from the flask module.

app = Flask(__name__) # app will be the object created by the constructor Flask. 

app.config['DEBUG'] = True #  the DEBUG configuration setting for the Flask application will be enabled. 

form = """
<html>
   <body>
       <form action="/hello" method="post">
           <label for "first_name">Name: </label>
           <input id="first-name" type="text" name="first_name" />
           <input type="submit" />
       </form>
   </body>
</html>
"""

@app.route("/form-inputs")
def display_form_inputs():
    return """
    <style>
    br {margin-bottom: 20px;}
    </style>
    <form method='POST'>
        <label>type=text
            <input name="user-name" type="text" />
        </label>
        <br>
        <label>type=password
            <input name="user-password" type="password" />
        </label>
        <br>
        <label>type=email
            <input name="user-email" type="email" />
        </label>
        <br>
        <input name="shopping-cart-id" value="0129384" type="hidden" />
        <br>
        <label>Ketchup
            <input type="checkbox" name="cb1" value="first-cb" />
        </label>
        <br>
        <label>Mustard
            <input type="checkbox" name="cb2" value="second-cb" />
        </label>
        <br>
        <label>Small
            <input type="radio" name="coffee-size" value="sm" />
        </label>
        <label>Medium
            <input type="radio" name="coffee-size" value="med" />
        </label>
        <label>Large
            <input type="radio" name="coffee-size" value="lg" />
        </label>
        <br>
        <label>Your life story
            <textarea name="life-story"></textarea>
        </label>
        <br>
        <label>LaunchCode Hub
            <select name="lc-hub">
                <option value="kc">Kansas City</option>
                <option value="mia">Miami</option>
                <option value="ri">Providence</option>
                <option value="sea">Seattle</option>
                <option value="pdx">Portland</option>
            </select>
        </label>
        <br>
        <input type="submit" />
    </form>
    """

@app.route("/")
def index():
    return form

@app.route("/form-inputs", methods=['POST'])
def print_orderform_values():
    resp=""
    for field in request.form.keys():
        resp += "<b>{key}</b>: {value}</b><br>".format(key=field, 
        value=request.form[field])
    return resp

app.run() 
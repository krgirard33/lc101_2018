from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2
import tasklist.py

template_dir = os.path.join(os.path.dirname(__file__),
    'templates')

jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(template_dir), autoescape=True
)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('hello_form.html')

@app.route('/hello', methods=['POST'])
def hello():
    first_name = request.form['first_name']
    return render_template('hello_greeting.html', name=first_name)

app.run()

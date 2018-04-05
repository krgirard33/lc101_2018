from flask import Flask, redirect, request
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__),
    'templates')

jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(template_dir), autoescape=True
)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/signup', methods=['POST'])
def signup_data():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
    
    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

@app.route('/signup')
def signup():
    user_info = request.args.get('user-info')
    template = jinja_env.get_template('signup_form.html')
    return template.render(user_info=user_info)


app.run()
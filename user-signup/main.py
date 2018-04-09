from flask import Flask, redirect, request
import cgi
import os
import jinja2
import re

template_dir = os.path.join(os.path.dirname(__file__),
    'templates')

jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(template_dir), autoescape=True
)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/signup')
def display_signup_form():
    template = jinja_env.get_template('signup_form.html')
    return template.render()

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

    if not username:
        username_error = 'You left this blank'
        username = ''
    else:
        try:
            if not re.match(r^(?=.*\d)(?=.*[a-zA-Z]).{8,20}$):
        except expression as identifier:
            pass
    
    if not password:
        password_error = 'You left this blank'
        password = ''
    
    if not username_error and not password_error:
        username = username
        return redirect('/welcome?username={0}'.format(username))

@app.route('/welcome')
def welcome():
    user_info = request.args.get('user-info')
    template = jinja_env.get_template('welcome.html')
    return template.render(user_info=user_info)

app.run()
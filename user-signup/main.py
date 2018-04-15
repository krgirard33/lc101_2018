from flask import Flask, redirect, request, render_template
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
    return render_template('signup_form.html', username='', username_error='', password='', 
        password_error='', verify='', verify_error='', email='', email_error='')

@app.route('/signup', methods=['POST'])
def signup_data():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email_add = request.form['email_add']
    
    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''
    have_error = False

    # validate username
    if not username:
        username_error = 'You left this blank'
        have_error = True
    elif ' ' in username:
        username_error = 'No spaces allowed'
        have_error = True
    elif len(username) < 3 or len(username) > 20:
            username_error = 'Must be between 3 & 20 characters long.'
            have_error = True
    else: 
        username = request.form['username']

    # validate password
    if not password:
        password_error = 'You left this blank'
        password = ''
        have_error = True
    elif ' ' in password:
        password_error = 'No spaces allowed'
        have_error = True
    else:
        if len(password) < 3 and len(password) > 20:
            password_error = 'Must be between 3 & 20 characters long.'
            have_error = True

    # validate verify
    if verify != password:
        verify_error = "These do not match!"
        have_error = True 

    # validate email
    if not email_add:
            email_error = ''
    elif ' ' in email_add or not '@' in email_add or not '.' in email_add:
        email_error = 'Does not compute. Please enter valid email'
        email_add = request.form['email_add']
        have_error = True
    
    if have_error == False:
        username = cgi.escape(username)
        return redirect('/welcome?username={0}'.format(username))
    else:
        email_add = cgi.escape(email_add)
        username = cgi.escape(username)
        return render_template('signup_form.html',username=username, email_add=email_add, 
        username_error=username_error,password_error=password_error,verify_error=verify_error,
        email_error=email_error)

@app.route('/welcome')
def welcome():
    username = request.args.get('username')
    username = cgi.escape(username)
    return render_template('welcome.html', username=username)

app.run()
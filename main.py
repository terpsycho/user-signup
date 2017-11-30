from flask import Flask, request, redirect
import os 
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))

app = Flask(__name__)
app.config['DEBUG'] = True

  
@app.route('/')
def info():
    template = jinja_env.get_template('signup_form.html')
    return template.render()


@app.route('/info', methods=['POST'])
def validate_info():

    username = request.form['username']
    password = request.form['password']
    pwverify = request.form['pwverify']
    email = request.form['email']

    username_error = ''
    password_error = ''
    pwverify_error = ''
    email_error = ''

    if not is_valid_username(username):
        username_error = "Not a valid username."
    
    #if not is_valid_username(password):
        #password_error = 'Not a valid password.'
    
    #if not is_valid_username(pwverify):
        #pwverify_error = "Passwords do not match."

    #if not is_valid_username(email):
        #email_error = "Not a valid email."


    def is_valid_username(name):
       try: 
            name is "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
            return True

       except ValueError:
            return False

@app.route("/hello", methods=['POST'])
def hello():
    username=''
    firstname = request.form['username']
    return '<h1> Hello, ' + firstname + '</h1>'

#@app.route("/")
#def index():
    #return form

app.run()

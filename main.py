from flask import Flask, request, redirect

app = Flask(__name__)
app.config['DEBUG'] = True


form = """
<!DOCTYPE HTML>
<style> .error {{ color: red;}}

 </style>

<html>
    <head>
        <style>
            
        </style>
    </head>
    <body>
    <form>
      <h1>Signup</h1>
      <form method="post">

      <label for="username" >Username</label>
      <input name="username" type="text" value >
      <p class="error" name="username_error"></p> <br>

      <label for="password" >Password</label>
      <input name="password" type="password" value>
      <p class="error" name ="password_error"></p> <br>

      <label for="pwverify" >Verify Password</label>
      <input name="pwverify" type="password" value>
      <p class="error" name ="pwverify_error"></p> <br>

      <label for="email" >Email (optional)</label>
      <input name="email" type="text" value>
      <p class="error" name= 'email_error'></p> <br>

      <input type="submit">
        </form>
    </body>
</html>
"""


@app.route("/")
def index():
    return form
   
@app.route('/info')
def info():
    return form.format( username= '', username_error= '', password='', password_error= '',
    pwverify='', pwverify_error='', email= '', email_error=''
    )


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
    
    if not is_valid_username(password):
        password_error = 'Not a valid password.'
    
    if not is_valid_username(pwverify):
        pwverify_error = "Passwords do not match."

    if not is_valid_username(email):
        email_error = "Not a valid email."


    def is_valid_username(name):
        try: 
            int(name)
            return True

        except ValueError:
            return False

@app.route("/hello", methods=['POST'])
def hello():
    username=''
    firstname = request.form['username']
    return '<h1> Hello, ' + firstname + '</h1>'



app.run()

from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True


form = """
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
    <form>
      <h1>Signup</h1>
      <form method="post">

      <label for="username" >Username</label>
      <input name="username" type="text" value>
      <span class="error"></span> <br>

      <label for="password" >Password</label>
      <input name="password" type="password" value>
      <span class="error"></span> <br>

      <label for="pwverify" >Verify Password</label>
      <input name="pwverify" type="password" value>
      <span class="error"></span> <br>

      <label for="email" >Email (optional)</label>
      <input name="email" type="text" value>
      <span class="error"></span> <br>

      <input type="submit">
        </form>
    </body>
</html>
"""
@app.route("/")
def index():
    return form

app.run()




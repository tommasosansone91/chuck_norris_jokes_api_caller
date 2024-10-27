from flask import Flask, render_template

from markupsafe import escape
 
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# a simple page that says hello
@app.route('/hello')
def hello():
    return '<h1>Welcome on Chuck Norris Jokes app!</h1>'
    
if __name__ == "__main__":
    app.run()
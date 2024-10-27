from flask import Flask, render_template
from flask import request

from markupsafe import escape
 
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route('/hello')
def hello():
    return '<h1>Welcome on Chuck Norris Jokes app!</h1>'
    

@app.route('/helloname/')
def helloname():
    name = request.args.get('name', 'You')
    # http://127.0.0.1:5000/helloname/?name=mario
    return f'<h1>Welcome on Chuck Norris Jokes app, {name}!</h1>' 
    

if __name__ == "__main__":
    app.run()
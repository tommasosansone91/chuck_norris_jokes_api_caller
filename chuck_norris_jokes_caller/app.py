import os

from flask import Flask
from flask import render_template
from flask import request

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from markupsafe import escape

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'chuck_norris_jokes_caller.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)
 


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



class Joke(db.Model):

    __tablename__ = 'joke'

    id = db.Column(db.Integer,primary_key=True)
    is_active = db.Column(db.Boolean, default=True)

    def __init__(self, is_active):
        self.is_active = is_active

    def __repr__(self):

        return f"Joke n.{self.id} (is active: {self.is_active})"




if __name__ == "__main__":
    app.run()
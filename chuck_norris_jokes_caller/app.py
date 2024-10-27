import os
import time

from flask import Flask
from flask import render_template
from flask import request

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from sqlalchemy import func

from db_queries import \
    GET_JOKES_BY_FREE_TEXT

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

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    is_active = db.Column(db.Boolean, default=True)

    def __init__(self, id=None):
        # self.is_active = is_active # do not put it or it will conflict with default=True

        if id is not None:
            self.id = id

        # do not remove the init or there will be no initialization for id, if init will be given in input
        pass

    def __repr__(self):

        return f"Joke n.{self.id} (is active: {self.is_active})"



class JokeVersion(db.Model):

    __tablename__ = 'joke_version'

    id = db.Column(db.Integer, autoincrement=True)
    joke_id = db.Column(db.Integer, nullable=False)
    creation_timestamp = db.Column(db.Integer, nullable=False, default=lambda: int(time.time()))
    content = db.Column(db.Text, nullable=False)

    # comosite pk
    __table_args__ = (
        db.PrimaryKeyConstraint('id', 'joke_id'),
    )

    def __init__(self, joke_id, content, id=None, creation_timestamp=None):
        
        if id is not None:
            self.id = id

        self.joke_id = joke_id
        self.creation_timestamp = creation_timestamp
        self.content = content
        

    def __repr__(self):

        return f"Version n.{self.id} of Joke n.{self.joke_id}"

    

if __name__ == "__main__":
    app.run()
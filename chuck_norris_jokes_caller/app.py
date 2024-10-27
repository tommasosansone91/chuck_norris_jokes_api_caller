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


    # @classmethod
    # # this is to tell that this method is not of my instance, but of my class
    # def get_most_recent_joke_version_by_joke_id(this_class, joke_id):
        
    #     result = (
    #         this_class.query
    #         .filter_by(joke_id=joke_id)
    #         .order_by(this_class.creation_timestamp.desc())
    #         .first()
    #     )
    
    #     return result
    
    # # most_recent_joke_version_for_joke_n34 = JokeVersion.get_most_recent_joke_version_by_joke_id(34)


    # @classmethod
    # def get_most_recent_joke_version_listfor_each_joke_id(this_class):

    #     # get_most_recent_joke_version_by_joke_id in another way
    #     subquery = (
    #         db.session.query(
    #             this_class.joke_id,
    #             func.max(this_class.creation_timestamp).label('max_creation_timestamp')
    #         )
    #         .group_by(this_class.joke_id)
    #         .subquery()
    #     )


    #     latest_versions = (
    #         db.session.query(this_class)
    #         .join(
    #             subquery,
    #             (this_class.joke_id == subquery.c.joke_id) & 
    #             (this_class.creation_timestamp == subquery.c.max_creation_timestamp)
    #         )
    #         .all()
    #     )
        
    #     return latest_versions
    

if __name__ == "__main__":
    app.run()
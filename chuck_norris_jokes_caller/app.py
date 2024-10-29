import os

from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

sqlite_db_path = os.path.join(basedir, 'chuck_norris_jokes_caller.sqlite')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + sqlite_db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app,db)

from api import \
    index, \
    helloname, \
    get_jokes_by_free_text, \
    get_jokes_by_id, \
    delete_joke_by_id, \
    add_joke, \
    update_joke_by_id
 

if __name__ == "__main__":
    app.run()
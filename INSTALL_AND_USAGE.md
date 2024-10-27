# install and usage

Please read this file and follow its instructions to install, setup, run and operate the application.

## install

    virtualenv venv

    source venv/bin/activate

    cat requirements.txt | xargs -n 1 pip install


## usage

### apply migrations

export the app script path as bash variable

    export FLASK_APP=chuck_norris_jokes_caller/app.py

initialize the db migration gear, it will create a folder at path `migrations`.<br>
You should ignore the error in case a folder `migrations` is already present/versioned in the project.

    flask db init  # create migration required files

save the changes to DB structure

    flask db migrate -m "< migration message here >"

apply the changes to DB structure

    flask db upgrade 


every time the DB structure is changed you have to run

    flask db migrate -m "< migration message here >"

    flask db upgrade  # the same of django's makemigrations


### populate db with test data

    python chuck_norris_jokes_caller/populate_database.py

In case you need to manipulate db data via SQL

    sqlite3 chuck_norris_jokes_caller/chuck_norris_jokes_caller.sqlite


### run

    flask --app chuck_norris_jokes_caller/app run --debug

>[!WARNING]
> do not add `--debug` in production!
# SQLalchemy database migration gear

### apply migrations

export the app script path as bash variable

    export FLASK_APP=chuck_norris_jokes_caller/app.py

Initialize the db migration gear: it will create a folder at path `migrations`.<br>

> [!TIP]
> You should ignore the error in case a folder `migrations` is already present/versioned in the project.

> [!NOTE]
> In case you deleted migrations and you want to init the db again:
> 
>     sqlite3 chuck_norris_jokes_caller/chuck_norris_jokes_caller.sqlite
>     
>         delete from alembic_version;  

create migration required files

    flask db init

save the changes to DB structure

    flask db migrate -m "< migration message here>"

apply the changes to DB structure

    flask db upgrade 

> [!NOTE]
> Every time the DB structure is changed, you have to run
> 
>     flask db migrate -m "< migration message here>"
> 
>     flask db upgrade

> [!NOTE]
> Every time you open a bash session or terminal and want to operate the migrations, you have to run
> 
>     export FLASK_APP=chuck_norris_jokes_caller/app.py


> [!WARNING]

> migrations do not affect changes in properties of field such as primary key, uniqueness, blankness, non-null ness...
# local app

chucknorrisjokeslocal

works via postman, no forms.

## DB

### tables

joke

id int pk
active bool


joke_version

id int pk
joke_id int pk
creation_timestamp INTEGER
content text



## APIs

### `GET /jokes/?query={query}`
Free text search endpoint. You should take local and remote search results into consideration.

    select 
        * 
    from 
        joke j
        join joke_version jv on(
                j.id = jv.joke_id, 
                )
    where
        jv.content ilike '%<query>%'
        and j.active = True
        and jv.latest = True


### `POST /api/jokes/`
Endpoint to create joke locally.

    

    insert into jokes


### `GET /api/jokes/{id}`
Endpoint to retrieve a joke by unique id. You should take local and remote results into consideration.

### `PUT /api/jokes/{id}`
Endpoint to update a joke by unique id. If the joke does not exist, return 404 not found. But if it does, store a updated version locally. Any subsequent reads should only see this updated version.

### `DELETE /api/jokes/{id}`
Endpoint to delete a joke by unique id. If the joke does not exist, return 404 not found. But if it does, mark the joke locally as deleted. Any subsequent reads should *NOT* see this joke.

it says "mark the joke locally as deleted" and not "mark the joke **version** locally as deleted


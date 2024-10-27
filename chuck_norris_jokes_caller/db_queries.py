

GET_JOKES_BY_FREE_TEXT = """
select 
    * 
from 
    joke j
    join joke_version jv on(
            j.id = jv.joke_id
            )
where
    lower(jv.content) like '%{}%'
    and j.active = True
    and jv.latest = True
"""
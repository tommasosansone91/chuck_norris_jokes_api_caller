DROP TABLE IF EXISTS joke;
DROP TABLE IF EXISTS joke_version;

CREATE TABLE joke (
    id INTEGER,
    active BOOLEAN,
    PRIMARY KEY (id)
);

CREATE TABLE joke_version (
    id INTEGER,
    joke_id INTEGER,
    creation_timestamp INTEGER,
    content TEXT,
    PRIMARY KEY (id, joke_id)
);

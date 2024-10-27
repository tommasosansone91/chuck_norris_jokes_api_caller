# install and usage

## install

    virtualenv venv

    source venv/bin/activate

    cat requirements.txt | xargs -n 1 pip install

# usage

## run

    flask --app chuck_norris_jokes_caller/app run --debug

>[!WARNING]
> do not add `--debug` in production!
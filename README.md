## Installing on a local machine
This project requires python 3.10. Deps are managed by [pip-tools](https://github.com/jazzband/pip-tools)

Install requirements:

```bash
$ pip install --upgrade pip pip-tools
$ pip-sync requirements.txt
```

Run the server:

```bash
$ cp src/.env.example src/.env  # default environment variables
$ uvicorn src.main:app
```

Testing:
```bash
# run lint
$ make lint

# run unit tests
$ make test
```

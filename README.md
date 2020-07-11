# cookbook

Store, read, and search your favorite recipes.

## Setup

### System dependencies

Install [PostgreSQL](https://www.postgresql.org/) locally. Once PostgreSQL is up and running, create a user and its database:

``` BASH
$ sudo -iu postgres
$ psql
$ CREATE USER cb_user WITH PASSWORD 'cookbook'; ALTER USER cb_user CREATEDB;
$ CREATE DATABASE db_cb OWNER cb_user;
```

## Test
```bash
$ python -m pytest tests/
```

## Run

```bash
export $(cat .env)
$ pip install -e .
```

### Save a recipe

```bash
$ cookbook save -u http://example.com -n Example
```

### List recipes

```bash
$ cookbook browse
```

## Contributing

```bash
$ alembic upgrade head
$ pip install -e .[dev]
$ pre-commit install
```

# cookbook

Store, read, and search your favorite recipes through command line.

## Example Usage

```bash
$ cookbook save -u http://example.com -n Example
```

```bash
$ cookbook view Example
```

## Setup

### System dependencies

Install [PostgreSQL](https://www.postgresql.org/) locally. Once PostgreSQL is up and running, create a user and its database:

``` bash
$ sudo -iu postgres
$ psql
$ CREATE USER cb_user WITH PASSWORD 'cookbook'; ALTER USER cb_user CREATEDB;
$ CREATE DATABASE db_cb OWNER cb_user;
```

### Environment variables

Cookbook relies on several env variables which contain the database login information. For example

```
DB_DRIVER=postgresql
DB_HOST=localhost
DB_PORT=5432
DB_USER=cb_user
DB_PWD=cookbook
DB_NAME=db_cb
```

* DB_DRIVER describes the type of driver/database used (postgresql, mysql...)
* DB_HOST is the location address of the database
* DB_PORT port where the database is listening
* DB_USER is the username for connecting to the database
* DB_PWD is the password for connecting to the database
* DB_NAME represents the name of the database where the recipe data will be stored

One the variables are defined (assuming it's an .env file), export them

```bash
export $(cat .env)
```

## Run

```bash
$ pip install -e .
$ alembic upgrade head
```

### Test
```bash
$ python -m pytest tests/
```

### Getting help

```bash
$ cookbook --help
```

### Save a recipe

```bash
$ cookbook save -u http://example.com -n Example
```

* -u is the url of the recipe
* -n is the name under which it will be saved

### List recipes

```bash
$ cookbook browse
```

Returns a list of names of all the saved recipes.

### View a stored recipe

```bash
$ cookbook view Example
```

View take as an argument a recipe name.

### Find a recipe

Find a recipe by searching for a part of it's name

```bash
$ cookbook find am
```

Should return 'Example'. Find takes as it's argument a part of the recipe name.

### Delete a recipe

```bash
$ cookbook delete Example
```

Will delete all recipes whose name exactly matches 'Example'. Delete takes as it's argument the recipe name.

## Contributing

```bash
$ pip install -e .[dev]
$ alembic upgrade head
$ pre-commit install
```

Cookbook relies on [alembic](https://alembic.sqlalchemy.org) for database migrations.

It also uses on [pre-commit](https://pre-commit.com/) hooks which run [flake8](https://gitlab.com/pycqa/flake8) and [black](https://black.readthedocs.io/en/stable/) code formatter before commmitting. This means that when you commit, both tools will run and you will fail to commit if tools report any errors. Fix the reported errors and commit again.

Finally, Cookbook uses [towncrier](https://towncrier.readthedocs.io/en/actual-freaking-docs/index.html) for [changelog](https://changelog.md/) management. Add a description file of your changes into .changelog.d folder. For example name the file `001.feature`. When you commit the code,
run

```bash
$ towncrier --version=x.y.z
```

This will add your changes to CHANGELOG.md and delete the .feature file. Commit-ammend this.

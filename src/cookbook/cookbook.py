import urllib.request
import click

from . import Session
from . import models as db


PATH = "/home/vedran/Documents/"


@click.group()
def cookbook():
    pass


@cookbook.command()
@click.option("-u", "--url", help="URL of the recipe to save")
@click.option("-n", "--name", "recipe_name", help="Save recipe under this name")
def save(url, recipe_name):
    response = urllib.request.urlopen(url)
    recipe = response.read()
    recipe_decoded = recipe.decode("utf-8")
    store_recipe(recipe_decoded, recipe_name)


@cookbook.command()
def browse():
    session = Session()
    contents = db.fetch_all(session)
    session.close()

    for content in contents:
        click.echo(content[0])


@cookbook.command()
@click.argument("recipe_name")
def view(recipe_name):
    # os.system(f"firefox {PATH}{filename}")
    session = Session()
    recipe = db.fetch(session, recipe_name)
    session.close()

    click.echo(recipe)


def store_recipe(content, saved_name):
    session = Session()
    db.store(session, saved_name, content)
    session.close()

    click.echo(f"{saved_name} saved")

import click

from requests import get

from . import Session
from . import models as db


@click.group()
def cookbook():
    # Just for grouping commands
    pass


@cookbook.command()
@click.option("-u", "--url", help="URL of the recipe to save")
@click.option("-n", "--name", "recipe_name", help="Save recipe under this name")
def save(url, recipe_name):
    """ Save the recipe from a given URL under the given name

        :param -u URL of the recipe to save
        :type u string
        :param -n Save recipe under this name
        :type n string
    """
    response = get(url)
    recipe = response.content
    recipe_decoded = recipe.decode("utf-8")
    store_recipe(recipe_decoded, recipe_name)


@cookbook.command()
def browse():
    """ Browse through the list of stored recipes

        :returns Lists stored recipes
    """
    session = Session()
    contents = db.fetch_all(session)
    session.close()

    for content in contents:
        click.echo(content[0])


@cookbook.command()
@click.argument("recipe_name")
def view(recipe_name):
    """ Open a particular recipe for reading

        :param recipe_name Name of the recipe to be opened
        :type strig
        :returns The required recipe
    """
    session = Session()
    recipe = db.fetch(session, recipe_name)
    session.close()

    click.echo(recipe)


@cookbook.command()
@click.argument("recipe_part")
def find(recipe_part):
    """ Find the stored recipe given a part of it's name

        :param recipe_part Part of the name of the recipe you are looking for
        :type string
        :returns Names of the recipes matching the part given
    """
    session = Session()
    recipes = db.find(session, recipe_part)

    for recipe in recipes:
        click.echo(recipe.name)
    session.close()


@cookbook.command()
@click.argument("recipe_name")
def delete(recipe_name):
    """ Delete the given recipe

        :param recipe_name Name of the recipe to be deleted
        :type string
    """
    session = Session()
    db.delete(session, recipe_name)
    session.close()


def store_recipe(content, saved_name):
    session = Session()
    db.store(session, saved_name, content)
    session.close()

    click.echo(f"{saved_name} saved")

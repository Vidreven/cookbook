import urllib.request
import click
import os


PATH = "/home/vedran/Documents/"


@click.group()
def cookbook():
    pass


@cookbook.command()
@click.option("-u", "--url", help="URL of the recipe to save")
@click.option("-n", "--name", "saved_name", help="Save recipe under this name")
def save(url, saved_name):
    response = urllib.request.urlopen(url)
    recipe = response.read()
    store_recipe(recipe, saved_name)


@cookbook.command()
def browse():
    contents = os.listdir(PATH)

    for content in contents:
        click.echo(content)


@cookbook.command()
@click.argument("filename")
def view(filename):
    os.system(f"firefox {PATH}{filename}")


def store_recipe(content, saved_name):
    filepath = f"{PATH}{saved_name}.html"
    with open(filepath, "w") as recipe:
        recipe.write(content.decode("utf-8"))
        click.echo(f"{saved_name} saved")

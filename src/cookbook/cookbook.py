import urllib.request
import click


@click.command()
@click.option("-s", "--save", "url", help="URL of the recipe to save")
@click.option("-n", "--name", "saved_name", help="Save recipe under this name")
def download_recipe(url, saved_name):
    response = urllib.request.urlopen(url)
    recipe = response.read()
    store_recipe(recipe, saved_name)


def store_recipe(content, saved_name):
    filepath = f"/home/vedran/Documents/{saved_name}.html"
    with open(filepath, "w") as recipe:
        recipe.write(content.decode("utf-8"))
        click.echo(f"{saved_name} saved")

import urllib.request


def download_recipe(url):
    response = urllib.request.urlopen(url)
    return response.read()


url = "https://www.allrecipes.com/recipe/244929/lemon-meringue-cheesecake"
recipe = download_recipe(url)
print(recipe)

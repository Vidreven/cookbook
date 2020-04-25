import urllib.request


def download_recipe(url):
    response = urllib.request.urlopen(url)
    return response.read()

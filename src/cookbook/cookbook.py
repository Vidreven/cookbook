import urllib.request

url = "https://www.allrecipes.com/recipe/244929/lemon-meringue-cheesecake"

response = urllib.request.urlopen(url)
content = response.read()

print(content)

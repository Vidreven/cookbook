from src.cookbook import cookbook

def test_store_recipe():
    url = 'https://duckduckgo.com/'
    website = cookbook.download_recipe(url)

    assert len(website) > 0

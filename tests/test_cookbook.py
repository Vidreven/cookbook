from src.cookbook import cookbook


def test_download_recipe():
    url = 'http://example.com/'
    website = cookbook.download_recipe(url)

    assert len(website) > 0

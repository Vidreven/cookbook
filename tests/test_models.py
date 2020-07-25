import cookbook.models as db
from cookbook import Session


def test_store_and_fetch_recipe():
    recipe_name = "test recipe"
    recipe_text = "recipe text"
    session = Session()

    db.store(session, recipe_name, recipe_text)
    recipe_text_fetched = db.fetch(session, recipe_name)
    db.delete(session, recipe_name)
    session.close()

    assert recipe_text_fetched == recipe_text


def test_find():
    name_part = "test"
    recipe_name = "test recipe"
    recipe_text = "recipe text"
    session = Session()

    db.store(session, recipe_name, recipe_text)
    recipes = db.find(session, name_part)
    db.delete(session, recipe_name)
    session.close()

    for recipe in recipes:
        assert recipe.name == recipe_name

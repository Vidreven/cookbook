from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, VARCHAR, Text
from sqlalchemy.exc import StatementError


Base = declarative_base()


class Recipe(Base):
    __tablename__ = "recipe"

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(), nullable=False)
    recipe = Column(Text, nullable=False)

    def __init__(self, name, recipe):
        self.name = name
        self.recipe = recipe

    def __repr__(self):
        return f"Recipe<(name={self.name}, recipe={self.recipe})>"


def store(session, recipe_name, recipe_text):
    try:
        recipe = Recipe(recipe_name, recipe_text)
        session.add(recipe)
        session.commit()
    except StatementError as se:
        print(se)
        session.rollback()


def fetch(session, recipe_name):
    try:
        recipe = session.query(Recipe.recipe).filter_by(name=recipe_name)
        return recipe[0][0]
    except StatementError as se:
        print(se)


def fetch_all(session):
    try:
        recipe = session.query(Recipe.name).all()
        return recipe
    except StatementError as se:
        print(se)


def delete(session, recipe_name):
    try:
        recipes = session.query(Recipe).filter_by(name=recipe_name)
        for recipe in recipes:
            session.delete(recipe)
        session.commit()
    except StatementError as se:
        print(se)
        session.rollback()

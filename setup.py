from setuptools import setup, find_packages

setup(
    name="cookbook",
    version="1.0.1",
    author="Vidreven",
    description="Store, read, edit, comment and search your favorite recipes.",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    license="MIT license",
    install_requires=[
        "setuptools>=46.1.3",
        "click>=7.1.2",
        "psycopg2>=2.8.5",
        "SQLAlchemy>=1.3.18",
        "alembic>=1.4.2",
        "requests>=2.23.0",
    ],
    extras_require={"dev": ["pytest>=5.4.1", "pre-commit>=2.5.1", "towncrier>=19.2.0"]},
    entry_points="""
        [console_scripts]
        cookbook=cookbook.cookbook:cookbook
    """,
)

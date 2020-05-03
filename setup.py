from setuptools import setup, find_packages

setup(
    name="cookbook",
    version="0.2.0",
    author="Vidreven",
    description="Store, read, edit, comment and search your favorite recipes.",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    license="MIT license",

    entry_points='''
        [console_scripts]
        cookbook=cookbook.cookbook:download_recipe
    '''
)

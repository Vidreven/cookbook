# cookbook v0.1.3

Store, read, edit, comment and search your favorite recipes.

## Test
```bash
$ python -m pytest tests/
```

## Run

```bash
$ pip install -r requirements.txt
$ pip install -e .
$ python
>>> from cookbook.cookbook import download_recipe
>>> download_recipe('http://example.com')
```

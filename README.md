# cookbook v0.3.1

Store, read, edit, comment and search your favorite recipes.

## Test
```bash
$ python -m pytest tests/
```

## Run

```bash
$ pip install -r requirements.txt
$ pip install -e .
```

### Save a recipe

```bash
$ cookbook download_recipe -s http://example.com -o Example
```

### List recipes
```bash
$ cookbook list_recipes
```

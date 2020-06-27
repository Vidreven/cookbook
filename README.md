# cookbook

Store, read, edit, comment and search your favorite recipes.

## Test
```bash
$ python -m pytest tests/
```

## Run

```bash
$ pip install -e .
```

### Save a recipe

```bash
$ cookbook save -u http://example.com -n Example
```

### List recipes
```bash
$ cookbook browse
```

## Contributing

```bash
$ pip install -e .[dev]
$ pre-commit install
```

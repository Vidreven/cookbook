from src.cookbook import cookbook
from click.testing import CliRunner


def test_save():
    runner = CliRunner()
    url = "http://example.com/"
    recipe_name = "Example"

    result = runner.invoke(cookbook.save, ["-u", url, "-n", recipe_name])

    assert result.exit_code == 0
    assert result.output == "Example saved\n"

    runner.invoke(cookbook.delete, [recipe_name])


def test_browse():
    url = "http://example.com/"
    recipe_name = "Example"

    runner = CliRunner()
    runner.invoke(cookbook.save, ["-u", url, "-n", recipe_name])
    result = runner.invoke(cookbook.browse)
    runner.invoke(cookbook.delete, [recipe_name])

    assert result.exit_code == 0
    assert len(result.output) > 0


def test_view():
    url = "http://example.com/"
    recipe_name = "Example"

    runner = CliRunner()
    runner.invoke(cookbook.save, ["-u", url, "-n", recipe_name])
    result = runner.invoke(cookbook.view, [recipe_name])
    runner.invoke(cookbook.delete, [recipe_name])
    assert result.exit_code == 0
    assert len(result.output) > 0


def test_find():
    url = "http://example.com/"
    recipe_name = "Example"
    name_part = "am"

    runner = CliRunner()
    runner.invoke(cookbook.save, ["-u", url, "-n", recipe_name])
    result = runner.invoke(cookbook.find, [name_part])
    runner.invoke(cookbook.delete, [recipe_name])
    assert result.exit_code == 0
    assert result.output.strip() == recipe_name

from src.cookbook import cookbook
from click.testing import CliRunner

url = "http://example.com/"


def test_save():
    runner = CliRunner()
    recipe_name = "Example"

    result = runner.invoke(cookbook.save, ["-u", url, "-n", recipe_name])

    assert result.exit_code == 0
    assert result.output == "Example saved\n"

    runner.invoke(cookbook.delete, [recipe_name])


def test_browse():
    recipe_name = "Example"

    runner = CliRunner()
    runner.invoke(cookbook.save, ["-u", url, "-n", recipe_name])
    result = runner.invoke(cookbook.browse)
    runner.invoke(cookbook.delete, [recipe_name])

    assert result.exit_code == 0
    assert len(result.output) > 0


def test_view():
    recipe_name = "Example"

    runner = CliRunner()
    runner.invoke(cookbook.save, ["-u", url, "-n", recipe_name])
    result = runner.invoke(cookbook.view, [recipe_name])
    runner.invoke(cookbook.delete, [recipe_name])
    assert result.exit_code == 0
    assert len(result.output) > 0


def test_find():
    recipe_name = "Example"
    name_part = "am"

    runner = CliRunner()
    runner.invoke(cookbook.save, ["-u", url, "-n", recipe_name])
    result = runner.invoke(cookbook.find, [name_part])
    runner.invoke(cookbook.delete, [recipe_name])
    assert result.exit_code == 0
    assert result.output.strip() == recipe_name

from src.cookbook import cookbook
from click.testing import CliRunner


def test_save():
    runner = CliRunner()
    url = "http://example.com/"
    recipe_name = "Example"

    result = runner.invoke(cookbook.save, ["-u", url, "-n", recipe_name])

    assert result.exit_code == 0
    assert result.output == "Example saved\n"


def test_browse():
    runner = CliRunner()
    result = runner.invoke(cookbook.browse)

    assert result.exit_code == 0


def test_view():
    recipe_name = "Example"

    runner = CliRunner()
    result = runner.invoke(cookbook.view, [recipe_name])
    assert result.exit_code == 0
    assert len(result.output) > 0

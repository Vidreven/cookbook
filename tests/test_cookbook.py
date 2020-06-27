from src.cookbook import cookbook
from click.testing import CliRunner
from os import system


def test_save():
    runner = CliRunner()
    url = "http://example.com/"
    filename = "Example"

    result = runner.invoke(cookbook.save, ["-u", url, "-n", filename])

    assert result.exit_code == 0
    assert result.output == "Example saved\n"

    filepath = f"/home/vedran/Documents/{filename}.html"

    with open(filepath) as f:
        content = f.read()

    system(f"rm -f {filepath}")

    assert len(content) > 0


def test_browse():
    runner = CliRunner()
    result = runner.invoke(cookbook.browse)

    # captured_out = result.output.split('\n')

    assert result.exit_code == 0


def test_view():
    filepath = f"/home/vedran/Documents/Example.html"

    runner = CliRunner()
    result = runner.invoke(cookbook.view, [filepath])
    system(f"rm -f {filepath}")
    assert result.exit_code == 0

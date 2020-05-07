from src.cookbook import cookbook
from click.testing import CliRunner


def test_download_recipe():
    runner = CliRunner()
    url = "http://example.com/"
    filename = 'Example'

    result = runner.invoke(cookbook.download_recipe, ['-s', url, '-n', filename])
    
    assert result.exit_code == 0
    assert result.output == 'Example saved\n'

    filepath = f"/home/vedran/Documents/{filename}.html"

    with open(filepath) as f:
        content = f.read()

    assert len(content) > 0

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


    def test_list_recipes():
        runner = CliRunner()
        result = runner.invoke(cookbook.list_recipes)

        #captured_out = result.output.split('\n')

        assert result.exit_code == 0

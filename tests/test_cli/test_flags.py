from click.testing import CliRunner

from frontend.cli import weave


def test_weave_no_source_flag_excludes_source():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(
            weave,
            [
                "waterlevels",
                "--output-type",
                "summary",
                "--dry",
                "--no-wqp",
            ],
            standalone_mode=False,
        )

    assert result.exit_code == 0
    config = result.return_value
    assert config.use_source_wqp is False
    assert config.use_source_nwis is True

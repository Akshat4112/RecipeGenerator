import os
from unittest.mock import patch


def test_defaults():
    import config

    assert isinstance(config.DATABASE_PATH, str)
    assert isinstance(config.MODEL_NAME, str)
    assert isinstance(config.MAX_LENGTH, int)
    assert config.MAX_LENGTH > 0


def test_env_override():
    with patch.dict(os.environ, {"RECIPE_MAX_LENGTH": "300"}):
        import importlib

        import config

        importlib.reload(config)
        assert config.MAX_LENGTH == 300

    import importlib

    import config

    importlib.reload(config)

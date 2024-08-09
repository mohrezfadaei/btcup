from app.config import Config


def test_get_config(monkeypatch):
    monkeypatch.setenv("API_TOKEN", "test_api_token")
    config = Config(env_file=None)
    assert config.get("API_TOKEN") == "test_api_token"

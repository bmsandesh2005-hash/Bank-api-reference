import pytest

from app.core.config import Settings


def test_settings_uses_safe_local_default_secret_key(monkeypatch):
    monkeypatch.delenv("SECRET_KEY", raising=False)

    settings = Settings()

    assert settings.secret_key
    assert len(settings.secret_key) >= 32

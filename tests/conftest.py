import pytest


@pytest.fixture(autouse=True)
def _mock_streamlit_cache(monkeypatch):
    """Replace Streamlit cache decorators with identity functions for testing."""
    import streamlit as st

    def identity_decorator(*args, **kwargs):
        if len(args) == 1 and callable(args[0]):
            return args[0]
        return lambda fn: fn

    monkeypatch.setattr(st, "cache_data", identity_decorator)
    monkeypatch.setattr(st, "cache_resource", identity_decorator)


@pytest.fixture
def tmp_db(monkeypatch, tmp_path):
    """Provide a temporary database path for testing."""
    db_path = str(tmp_path / "test.db")
    monkeypatch.setattr("config.DATABASE_PATH", db_path)
    import db as db_module

    monkeypatch.setattr(db_module, "DATABASE_PATH", db_path)
    return db_path

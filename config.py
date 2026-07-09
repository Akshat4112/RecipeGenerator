import os

DATABASE_PATH: str = os.environ.get("RECIPE_DB_PATH", "textechdb781")
MODEL_NAME: str = os.environ.get("RECIPE_MODEL_NAME", "anonymous-german-nlp/german-gpt2")
LOCAL_MODEL_PATH: str = os.environ.get("RECIPE_LOCAL_MODEL_PATH", "./gpt2-gerchef")
MAX_LENGTH: int = int(os.environ.get("RECIPE_MAX_LENGTH", "200"))


def is_cloud() -> bool:
    """Return True when running on Streamlit Community Cloud (free tier, 1 GB RAM).

    Streamlit Cloud runs every app as the 'appuser' system user, so HOME is
    /home/appuser.  A STREAMLIT_CLOUD env var override lets operators force
    either mode explicitly.
    """
    explicit = os.environ.get("STREAMLIT_CLOUD", "").lower()
    if explicit in ("true", "1"):
        return True
    if explicit in ("false", "0"):
        return False
    return os.environ.get("HOME", "") == "/home/appuser"

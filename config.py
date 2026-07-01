import os

DATABASE_PATH: str = os.environ.get("RECIPE_DB_PATH", "textechdb781")
MODEL_NAME: str = os.environ.get("RECIPE_MODEL_NAME", "anonymous-german-nlp/german-gpt2")
LOCAL_MODEL_PATH: str = os.environ.get("RECIPE_LOCAL_MODEL_PATH", "./gpt2-gerchef")
MAX_LENGTH: int = int(os.environ.get("RECIPE_MAX_LENGTH", "200"))

# CLAUDE.md

## Project Overview

RecipeGenerator is a German recipe generation web application built with Streamlit. Users enter ingredients in German, and a GPT-2 model (running locally via HuggingFace Transformers) generates recipe instructions. The project was created as a Text Technology course project at Universitat Stuttgart.

The model (`anonymous-german-nlp/german-gpt2`, optionally fine-tuned as `gpt2-gerchef`) runs locally. Query history is stored in a local SQLite database.

## Tech Stack

- **Language:** Python 3.9+
- **Frontend:** Streamlit (multi-page app via custom `MultiApp` class, sidebar navigation)
- **ML Model:** GPT-2 (german-gpt2), local inference via HuggingFace Transformers
- **Database:** SQLite (file path configured in `config.py`)
- **Data Processing:** pandas, numpy, scikit-learn
- **Visualization:** Altair (bundled with Streamlit), matplotlib, seaborn
- **XML/Schema:** lxml, xmlschema
- **Linting:** ruff (configured in `pyproject.toml`)
- **Testing:** pytest (mocked Streamlit decorators in `tests/conftest.py`)
- **CI:** GitHub Actions (lint + test)
- **Deployment:** Docker (pre-downloads GPT-2 model)

## Directory Structure

```
├── app.py                  # Main entry point — runs the multi-page Streamlit app
├── multiapp.py             # MultiApp class for sidebar navigation via selectbox
├── config.py               # All configuration (model name, DB path, max length)
├── db.py                   # Shared database connection, auto-creates schema, migrations
├── model.py                # Local GPT-2 loading (@st.cache_resource) and generation
├── data_loader.py          # Shared @st.cache_data CSV loader for EDA and recipe search
├── database.py             # Standalone script to initialize/check the DB
├── requirements.txt        # Direct project dependencies only
├── requirements-dev.txt    # Dev dependencies (ruff, pytest)
├── pyproject.toml          # ruff + pytest configuration
├── Dockerfile              # Docker deployment with pre-downloaded model
├── .dockerignore
├── .gitignore
├── .github/workflows/ci.yml  # GitHub Actions CI (lint + test)
├── apps/                   # Streamlit page modules (each exports an app() function)
│   ├── __init__.py         # Package marker
│   ├── interactiveapp.py   # Homepage — ingredient input, generation controls, DB write
│   ├── recipe_search.py    # Recipe search/browse with filters and pagination
│   ├── history.py          # Generation history viewer with search
│   ├── dashboard.py        # Analytics dashboard — date filtering, charts, CSV export
│   ├── exploratoryDataAnalysis.py  # EDA with Altair charts
│   ├── whatitdoes.py       # App description page
│   ├── about_dataset.py    # Dataset metadata page
│   ├── aboutmlmodel.py     # GPT-2 architecture description
│   ├── xmlversion.py       # XML sample display
│   ├── dtdversion.py       # DTD schema display
│   ├── xsd.py              # XSD schema display
│   └── relaxng.py          # RelaxNG schema display
├── training/
│   └── train_gpt2.py       # Fine-tune german-gpt2 on recipe dataset
├── src/
│   └── ml_api.py           # Optional Flask API server for GPT-2 inference
├── tests/
│   ├── conftest.py         # Fixtures: mock Streamlit caches, temp DB path
│   ├── test_config.py      # Config defaults and env var overrides
│   ├── test_db.py          # Connection, table creation, insert/query, migration
│   ├── test_data_loader.py # CSV loading and column cleanup
│   └── test_model.py       # Prompt template and generation params (mocked pipeline)
├── data/
│   ├── raw/recipes.json    # Original recipe data (JSON)
│   └── processed/
│       ├── recipes_csv.csv # 12,190 recipes as CSV
│       └── recipes_xml.xml # Recipes in XML format
├── notebooks/              # Jupyter notebooks (EDA, data formats)
├── images/                 # Static images used in the Streamlit app
├── docs/                   # Project planning notes
└── LICENSE
```

## Running the App

```bash
pip install -r requirements.txt
streamlit run app.py
```

The model downloads automatically from HuggingFace on first run. If a fine-tuned model exists at `./gpt2-gerchef`, it will be used instead.

## Development

```bash
pip install -r requirements-dev.txt
ruff check .                # lint
ruff format --check .       # format check
python3 -m pytest tests/ -v # run tests
```

## Configuration

All settings are in `config.py` and can be overridden via environment variables:

| Variable | Default | Purpose |
|---|---|---|
| `RECIPE_DB_PATH` | `textechdb781` | SQLite database file path |
| `RECIPE_MODEL_NAME` | `anonymous-german-nlp/german-gpt2` | HuggingFace model/tokenizer name |
| `RECIPE_LOCAL_MODEL_PATH` | `./gpt2-gerchef` | Path to fine-tuned model (used if exists) |
| `RECIPE_MAX_LENGTH` | `200` | Max tokens for text generation |

## Key Architecture Patterns

### Multi-Page App

`app.py` uses `MultiApp` (from `multiapp.py`) to register page modules. Each module in `apps/` exports a single `app()` function. Pages are selected via `st.sidebar.selectbox`.

### Local Model

`model.py` loads the GPT-2 model once using `@st.cache_resource` and exposes `generate_recipe(ingredients, temperature, max_length, top_p)`. It uses a prompt template (`Zutaten: {ingredients}\n\nZubereitung:`) for structured output. It checks for a fine-tuned model at `LOCAL_MODEL_PATH` first, falls back to the base `MODEL_NAME`.

### Database

`db.py` provides `get_connection()` which returns a SQLite connection, auto-creates the `history` table if missing, and runs schema migrations (e.g., renaming `model` column to `generated_text`). Use as a context manager: `with get_connection() as conn:`.

The `history` table schema: `id` (autoincrement), `input_text`, `generated_text`, `date`.

### Data Loading

`data_loader.py` provides `load_recipes()` decorated with `@st.cache_data` for efficient CSV loading. Used by EDA and recipe search pages.

### Optional Flask API

`src/ml_api.py` can serve the model as a REST API (`POST /predict_text` with `{"text": "..."}`) for remote access. This is optional — the Streamlit app runs the model locally by default.

## Data

- **Source:** chefkoch.de (German cooking site)
- **Size:** 12,190 recipes
- **Fields:** Url, Instructions, Ingredients, Day, Name, Year, Month, Weekday
- **Formats:** JSON (raw), CSV and XML (processed)

## Training the Model

```bash
cd training
python train_gpt2.py
```

Output is saved to `./gpt2-gerchef`. Training config: 3 epochs, batch size 32, TensorBoard logging.

## Conventions

- All Streamlit page modules go in `apps/` and export a single `app()` function
- Database access goes through `db.get_connection()` — never create connections directly
- Model access goes through `model.generate_recipe()` — never load the model directly
- Data loading goes through `data_loader.load_recipes()` for cached CSV access
- Configuration goes in `config.py` with env var overrides
- Recipe data files go in `data/processed/` or `data/raw/`
- Static assets go in `images/`
- The app UI uses German text for all user-facing labels
- Use `ruff` for linting and formatting (configured in `pyproject.toml`)
- Tests mock Streamlit cache decorators via `conftest.py` fixtures

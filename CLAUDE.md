# CLAUDE.md

## Project Overview

RecipeGenerator is a German recipe generation web application built with Streamlit. Users enter ingredients in German, and a fine-tuned GPT-2 model generates recipe instructions. The project was created as a Text Technology course project at Universitat Stuttgart.

The ML model (GPT-2 fine-tuned on ~12,000 German recipes from chefkoch.de) is deployed on AWS EC2 and accessed via a Flask REST API. The Streamlit frontend calls this API and stores query history in a local SQLite database.

## Tech Stack

- **Language:** Python 3.9
- **Frontend:** Streamlit 1.4 (multi-page app via custom `MultiApp` class)
- **ML Model:** GPT-2 (german-gpt2 by anonymous-german-nlp), fine-tuned with HuggingFace Transformers 4.15
- **API:** Flask (deployed on AWS EC2 at port 5001)
- **Database:** SQLite (`textechdb781` file in project root)
- **Data Processing:** pandas, numpy, scikit-learn, matplotlib, seaborn
- **XML/Schema:** lxml, xmlschema (DTD, XSD, RelaxNG representations of recipe data)

## Directory Structure

```
├── app.py                  # Main entry point — runs the multi-page Streamlit app
├── multiapp.py             # MultiApp class for page navigation via selectbox
├── database.py             # Standalone script to initialize SQLite DB schema
├── textechdb781            # SQLite database file (user query history)
├── requirements.txt        # pip dependencies (pinned versions)
├── apps/                   # Streamlit page modules (each exports an app() function)
│   ├── interactiveapp.py   # Homepage — ingredient input, API call, DB write
│   ├── whatitdoes.py       # App description page
│   ├── about_dataset.py    # Dataset metadata page
│   ├── xmlversion.py       # XML sample display
│   ├── dtdversion.py       # DTD schema display
│   ├── xsd.py              # XSD schema display
│   ├── relaxng.py          # RelaxNG schema display
│   ├── exploratoryDataAnalysis.py  # EDA with charts (year/month/weekday distributions)
│   ├── aboutmlmodel.py     # GPT-2 architecture description
│   ├── dashboard.py        # Insight dashboard — top searched ingredients from DB
│   └── gpt2_german_recipes.py  # Model training script (not a Streamlit page)
├── src/
│   ├── ml_api.py           # Flask API server for GPT-2 inference
│   └── train.py            # Model training script (empty/stub)
├── data/
│   ├── raw/recipes.json    # Original recipe data (JSON)
│   └── processed/
│       ├── recipes_csv.csv # 12,190 recipes as CSV
│       └── recipes_xml.xml # Recipes in XML format
├── notebooks/
│   ├── EDA.ipynb           # Exploratory data analysis notebook
│   └── dataformats.ipynb   # Data format conversion notebook
├── images/                 # Static images used in the Streamlit app
├── docs/                   # Project planning notes
└── LICENSE                 # MIT License
```

## Running the App

```bash
pip install -r requirements.txt
streamlit run app.py
```

The app expects the GPT-2 API to be running on `http://3.20.227.146:5001` (AWS EC2). If the API is down, the recipe generation feature on the HomePage will fail.

## Running the API Server

The Flask API (`src/ml_api.py`) requires the fine-tuned model directory `./gpt2-gerchef` to exist locally:

```bash
cd src
python ml_api.py
```

This starts the API on port 5001 with a `/predict_text` POST endpoint.

## Key Architecture Patterns

### Multi-Page App

`app.py` uses `MultiApp` (from `multiapp.py`) to register page modules. Each module in `apps/` exports a single `app()` function that renders its Streamlit page. Pages are selected via a top-level `st.selectbox`.

### Database

SQLite stores user queries and model responses in a `history` table with columns: `id`, `input_text`, `model`, `date`. The DB file (`textechdb781`) lives in the project root. Run `database.py` once to initialize the schema.

### API Integration

`apps/interactiveapp.py` sends POST requests to the EC2-hosted Flask API with `{"text": "<ingredients>"}` and displays the generated recipe text.

## Data

- **Source:** chefkoch.de (German cooking site)
- **Size:** 12,190 recipes
- **Fields:** Url, Instructions, Ingredients, Day, Name, Year, Month, Weekday
- **Formats:** JSON (raw), CSV and XML (processed)

## Development Notes

- No CI/CD pipeline is configured
- No test suite exists
- No linter or formatter configuration is present
- The `requirements.txt` was generated with `pip freeze` and contains the full environment (180+ packages), not just direct dependencies
- The `src/` directory contains `__pycache__` with compiled modules from an earlier layout where source files lived there — the active Streamlit pages are in `apps/`
- `apps/gpt2_german_recipes.py` is a training script, not a Streamlit page (it is not registered in `app.py`)

## Conventions

- All Streamlit page modules go in `apps/` and export a single `app()` function
- Recipe data files go in `data/processed/` (derived) or `data/raw/` (original)
- Static assets (images) go in `images/`
- The app UI uses German text for user-facing labels ("Zutaten eingeben", "Da ist deine Rezepte!")
- Database interactions use raw `sqlite3` with inline SQL

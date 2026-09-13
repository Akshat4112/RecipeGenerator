# RecipeGenerator
Welcome! We are glad you have landed on our German Recipe Generator. The Recipe Generator is created to accept one or more ingredients in text format in the main central toolbar and to generate the procedure of a recipe that is done using the chosen ingredients. With Recipe Generator we want to help you find new recipes through which you can be able to employ food leftovers you have stuck in your fridge.<br>

There are 3 phases of our project:
1. Collect: In this phase we have collected the data from chefkoch.de, i.e. around 12,000 recipes. 
2. Prepare: In this phase we created XML, DTD, XSD, RelaxNG Schemas for it, also created the database using SQLite to store user query and model output data.
3. Access: In this phase we connected database with the web app from which functionality can be used.
 
### Technical Extensions
------------
1. Web App: we create the web app using Streamlit with sidebar navigation for easy access of the solution.
2. Machine Learning Model: we have used GPT-2 model and leveraged it using recipe data to generate recipes on certain ingredients. The model runs locally using HuggingFace Transformers with configurable generation parameters (temperature, top-p, max length).
3. Recipe Search: a searchable, filterable, paginated browser for the full 12,190-recipe dataset.
4. Generation History: a history page showing all past generations with search functionality.
5. Analytics Dashboard: date-range filtering, top ingredient charts, and CSV export.
6. Explorative Data Analysis: interactive EDA with Altair charts.
7. RelaxNG: We also created RelaxNG schema which is compact and simple and more natural representation of the document's structure. 
8. Testing & CI: pytest test suite with 9 tests, GitHub Actions CI (lint + test).
9. Docker: Dockerfile for containerized deployment with pre-downloaded model.

### Tech Stack
------------
* Python 3.9+ and its libraries
* Streamlit for the multi-page web app (sidebar navigation)
* HuggingFace Transformers for local GPT-2 inference
* SQLite for database
* Altair, matplotlib, seaborn for visualization
* ruff for linting, pytest for testing
* GitHub Actions for CI (lint + test)
* Docker for deployment

### Running the App
------------
```bash
pip install -r requirements.txt
streamlit run app.py
```

The model downloads automatically from HuggingFace on first run. If a fine-tuned model exists at `./gpt2-gerchef`, it will be used instead.

### Development
------------
```bash
pip install -r requirements-dev.txt
ruff check .                # lint
ruff format --check .       # format check
python3 -m pytest tests/ -v # run tests
```

### Docker
------------
```bash
docker build -t recipe-generator .
docker run -p 8501:8501 recipe-generator
```

### Configuration
------------
All settings are in `config.py` and can be overridden via environment variables:

| Variable | Default | Purpose |
|---|---|---|
| `RECIPE_DB_PATH` | `textechdb781` | SQLite database file path |
| `RECIPE_MODEL_NAME` | `anonymous-german-nlp/german-gpt2` | HuggingFace model name |
| `RECIPE_LOCAL_MODEL_PATH` | `./gpt2-gerchef` | Path to fine-tuned model |
| `RECIPE_MAX_LENGTH` | `200` | Max tokens for text generation |

### Directory structure of the project
------------

The directory structure of the recipe generator project looks like this: 

```
├── LICENSE
├── README.md             <- Project overview and documentation
├── config.py             <- Configuration (model paths, DB path, env vars)
├── db.py                 <- Shared database connection, schema setup, migrations
├── model.py              <- Local GPT-2 model loading and recipe generation
├── data_loader.py        <- Shared cached CSV loader for EDA and recipe search
├── app.py                <- Main entry point for the multi-page Streamlit app
├── multiapp.py           <- MultiApp framework for sidebar navigation
├── database.py           <- Standalone script to initialize and check the DB
├── requirements.txt      <- Direct project dependencies
├── requirements-dev.txt  <- Dev dependencies (ruff, pytest)
├── pyproject.toml        <- ruff + pytest configuration
├── Dockerfile            <- Docker deployment with pre-downloaded model
├── .dockerignore
├── .gitignore
├── .github
│   └── workflows
│       └── ci.yml        <- GitHub Actions CI (lint + test)
├── data
│   ├── processed         <- Processed data (CSV, XML)
│   └── raw               <- Original JSON data dump
├── notebooks             <- Jupyter notebooks (EDA, data format conversion)
├── apps                  <- Streamlit page modules (each exports an app() function)
│   ├── __init__.py       <- Package marker
│   ├── interactiveapp.py <- Homepage with ingredient input and generation controls
│   ├── recipe_search.py  <- Recipe search/browse with filters and pagination
│   ├── history.py        <- Generation history viewer with search
│   ├── dashboard.py      <- Analytics dashboard with date filtering and CSV export
│   ├── exploratoryDataAnalysis.py <- EDA with Altair charts
│   ├── about_dataset.py  <- Dataset description
│   ├── aboutmlmodel.py   <- GPT-2 model architecture info
│   ├── whatitdoes.py     <- App description page
│   ├── dtdversion.py     <- DTD schema display
│   ├── xmlversion.py     <- XML data display
│   ├── xsd.py            <- XSD schema display
│   └── relaxng.py        <- RelaxNG schema display
├── training
│   └── train_gpt2.py    <- Fine-tune german-gpt2 on recipe dataset
├── src
│   └── ml_api.py         <- Optional Flask API server for model inference
├── tests
│   ├── conftest.py       <- Fixtures: mock Streamlit caches, temp DB path
│   ├── test_config.py    <- Config defaults and env var overrides
│   ├── test_db.py        <- Connection, table creation, insert/query, migration
│   ├── test_data_loader.py <- CSV loading and column cleanup
│   └── test_model.py     <- Prompt template and generation params (mocked pipeline)
├── images                <- Static image assets for the webapp
└── docs                  <- Project planning notes

```

### Citation
------------
If you use this library for your publications, please cite it as:
```
author    = {Silvia Cunico},{Akshat Gupta}
title     = {Recipe Generator using GPT-2},
address   = {Universitat Stuttgart, Stuttgart, Germany},
year      = {2022},
month     = {February},
url       = {https://github.com/Akshat4112/RecipeGenerator}
```

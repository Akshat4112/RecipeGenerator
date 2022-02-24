# RecipeGenerator
Welcome! We are glad you have landed on our German Recipe Generator. The Recipe Generator is created to accept one or more ingredients in text format in the main central toolbar and to generate the procedure of a recipe that is done using the chosen ingredients. With Recipe Generator we want to help you find new recipes through which you can be able to employ food leftovers you have stuck in your fridge.<br>

There are 3 phases of our project:
1. Collect
2. Prepare 
3. Access

### Description of phases
------------
In Collect phase we have collected the data from chefkoch.de, i.e. around 12,000 recipes. 
In Prepare phase we created XML, DTD, XSD, RelaxNG Schemas for it, also created the database using SQLite to store user query and model output data.
In Access phase we connected database with the web app from which functionality can be used. 

### Technical Extensions
------------
1. Web App
2. Machine Learning Model
3. API Deployment
4. XML Technologies, Python Libraries

### Tech Stack
------------




### The resulting directory structure
------------

The directory structure of your new project looks like this: 

```
├── LICENSE
├── Makefile           <- Makefile with commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default Sphinx project; see sphinx-doc.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── data           <- Scripts to download or generate data
│   │   └── make_dataset.py
│   │
│   ├── features       <- Scripts to turn raw data into features for modeling
│   │   └── build_features.py
│   │
│   ├── models         <- Scripts to train models and then use trained models to make
│   │   │                 predictions
│   │   ├── predict_model.py
│   │   └── train_model.py
│   │
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
│       └── visualize.py
│
└── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io
```


### Installing development requirements
------------

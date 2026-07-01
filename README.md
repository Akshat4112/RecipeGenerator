# RecipeGenerator
Welcome! We are glad you have landed on our German Recipe Generator. The Recipe Generator is created to accept one or more ingredients in text format in the main central toolbar and to generate the procedure of a recipe that is done using the chosen ingredients. With Recipe Generator we want to help you find new recipes through which you can be able to employ food leftovers you have stuck in your fridge.<br>

There are 3 phases of our project:
1. Collect: In this phase we have collected the data from chefkoch.de, i.e. around 12,000 recipes. 
2. Prepare: In this phase we created XML, DTD, XSD, RelaxNG Schemas for it, also created the database using SQLite to store user query and model output data.
3. Access: In this phase we connected database with the web app from which functionality can be used.
 
### Technical Extensions
------------
1. Web App: we create the web app using streamlit for easy access of the solution. 
2. Machine Learning Model: we have used GPT-2 model and leveraged it using recipe data to generate recipes on certain ingredients. The model runs locally using HuggingFace Transformers.
3. RelaxNG: We also created RelaxNG schema which is compact and simple and more natural representation of the document's structure. 
4. Python Libraries: We have used various python libraries to support our objective such as pandas, lxml, sklearn, numpy, matplotlib, streamlit, transformers and others. 

### Tech Stack
------------
* Python 3.9+ and its libraries
* SQLite for database
* HuggingFace Transformers for local GPT-2 inference
* GitHub as VCS
* VSCode as Code Editor

### Directory structure of the project
------------

The directory structure of your recipe generator project looks like this: 

```
├── LICENSE
├── README.md             <- Project overview and documentation
├── config.py             <- Configuration (model paths, DB path, env vars)
├── db.py                 <- Shared database connection and schema setup
├── model.py              <- Local GPT-2 model loading and recipe generation
├── app.py                <- Main entry point for the multi-page Streamlit app
├── multiapp.py           <- MultiApp framework for Streamlit page navigation
├── database.py           <- Standalone script to initialize and check the DB
├── requirements.txt      <- Direct project dependencies
├── .gitignore            <- Git ignore rules
├── data
│   ├── processed         <- Processed data (CSV, XML)
│   └── raw               <- Original JSON data dump
├── notebooks             <- Jupyter notebooks (EDA, data format conversion)
├── apps                  <- Streamlit page modules (each exports an app() function)
│   ├── interactiveapp.py <- Homepage with ingredient input and local LLM generation
│   ├── about_dataset.py  <- Dataset description
│   ├── aboutmlmodel.py   <- GPT-2 model architecture info
│   ├── dashboard.py      <- Insight dashboard from DB query history
│   ├── exploratoryDataAnalysis.py <- EDA visualizations
│   ├── dtdversion.py     <- DTD schema display
│   ├── xmlversion.py     <- XML data display
│   ├── xsd.py            <- XSD schema display
│   ├── relaxng.py        <- RelaxNG schema display
│   ├── whatitdoes.py     <- App description page
│   └── gpt2_german_recipes.py <- Model training script
├── src
│   └── ml_api.py         <- Optional Flask API server for model inference
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

# RecipeGenerator
Welcome! We are glad you have landed on our German Recipe Generator. The Recipe Generator is created to accept one or more ingredients in text format in the main central toolbar and to generate the procedure of a recipe that is done using the chosen ingredients. With Recipe Generator we want to help you find new recipes through which you can be able to employ food leftovers you have stuck in your fridge.<br>

There are 3 phases of our project:
1. Collect: In this phase we have collected the data from chefkoch.de, i.e. around 12,000 recipes. 
2. Prepare: In this phase we created XML, DTD, XSD, RelaxNG Schemas for it, also created the database using SQLite to store user query and model output data.
3. Access: In this phase we connected database with the web app from which functionality can be used.
 
### Technical Extensions
------------
1. Web App: we create the web app using streamlit for easy access of the solution. 
2. Machine Learning Model: we have used GPT-2 model and leveraged it using recipe data toi generate recipes on certain ingredients. 
3. API Deployment: It is difficult to run GPT-2 model on a local system, so we have deployed it on EC2 and created the API on it using flask to setup the connection between API and web app.
4. RelaxNG: We also created RelaxNG schema which is compact and simple and more natural representation of the document's structure. 
5. Python Libraries: We have used various python libraries to support our objective such as pandas, lxml, sklearn, numpy, matplotlib, scipy, keras, streamlit, tensorflow, transformers and others. 

### Tech Stack
------------
* Python 3.9.1 and its libraries
* SQLite for database
* AWS EC2 for API endpoint
* Github as VCS
* VScode as Code Editor

### Directory structure of the project
------------

The directory structure of your recipe generator project looks like this: 

```
├── LICENSE
├── README.md          <- Tell about the project, WHat it does? How it does? Why it does?
├── data
│   ├── processed      <- The final, canonical data sets for modeling such as recipes_csv.csv, recipes_xml.xml, dtd, xsd and other processed files. 
│   └── raw            <- The original, immutable json data dump as recipes.json
│
│
├── models             <- Trained and serialized models, model predictions, or model summaries but it is placed on aws, not in project directory due to size limits.
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering), containes EDA and dataformats notebooks.
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated PPTs, Documents and screenshots for the app. 
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── apps                <- Source code for use in this project.
│   ├── about_dataset.py    <- containes function which tells about the dataset, data description.
│   │
│   ├── aboutmlmodel.py     <- contains function which describes about GPT2 Machine Learning Model used? and how it is being trained?
│   │
│   ├── dashboard.py        <- contains function to create a dabase connection
│   │
│   ├── dtdversion.py       <- contains the document type definition of our xml document 
│   │
│   └── exploratoryDataAnalysis.py  <- scripts to create exploratory and results oriented visualizations
│   │
│   ├── gpt2_german_recipes.py       <- contains a function to build text files from the json dataset, transformer model code
│   │
│   ├── interactiveapp.py            <- contains a function to create the Interactive app, Homepage, API call and database dump. 
│   │
│   ├── relaxng.py                   <- contains a function to show the RelaxNG Version of the dataset.
│   │
│   ├── whatitdoes.py                <- contains a function to tell user about the app, what it does?
│   │
│   ├── xmlversion.py                <- contains our extracted data written in xml format
│   │
│   ├── xsd.py                       <- contains the xsd for our XML data, that defines it structure 
│── images                           <- It has image resources used on the webapp. 
│
├──app.py                            <- Main python script to run the multipage streamlit app
│
├──database.py                       <- contains the code to create the dataset
│
├──multiapp.py                       <- function to support multiapp view for streamlit app
│
├──texttechdb781                     <- SQlite database file

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
}
```

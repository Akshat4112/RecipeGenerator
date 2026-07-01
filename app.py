import streamlit as st

from apps import (
    about_dataset,
    aboutmlmodel,
    dashboard,
    dtdversion,
    exploratoryDataAnalysis,
    history,
    interactiveapp,
    recipe_search,
    relaxng,
    whatitdoes,
    xmlversion,
    xsd,
)
from multiapp import MultiApp

st.set_page_config(
    page_title="Deutscher Rezeptgenerator",
    page_icon="\U0001F373",
    layout="wide",
)

st.title("Deutscher Rezeptgenerator")
app = MultiApp()
app.add_app("Startseite", interactiveapp.app)
app.add_app("Rezeptsuche", recipe_search.app)
app.add_app("Rezeptverlauf", history.app)
app.add_app("Was macht der Rezeptgenerator?", whatitdoes.app)
app.add_app("Über den Datensatz", about_dataset.app)
app.add_app("XML-Version der Daten", xmlversion.app)
app.add_app("DTD-Version der Daten", dtdversion.app)
app.add_app("XSD-Version der Daten", xsd.app)
app.add_app("RelaxNG-Version der Daten", relaxng.app)
app.add_app("Explorative Datenanalyse", exploratoryDataAnalysis.app)
app.add_app("Über das ML-Modell", aboutmlmodel.app)
app.add_app("Analyse-Dashboard", dashboard.app)
app.run()

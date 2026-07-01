import streamlit as st
from apps import about_dataset, aboutmlmodel, dashboard, dtdversion, exploratoryDataAnalysis, interactiveapp, relaxng, whatitdoes, xmlversion, xsd
from multiapp import MultiApp

st.title("Recipe Generator App")
app = MultiApp()
app.add_app("HomePage", interactiveapp.app)
app.add_app("What Recipe Generator Does?", whatitdoes.app)
app.add_app("About Dataset", about_dataset.app)
app.add_app("XML Version of data", xmlversion.app)
app.add_app("DTD Version of data", dtdversion.app)
app.add_app("XSD Version of data", xsd.app)
app.add_app("RELAXNG Version of data", relaxng.app)
app.add_app("Exploratory Data Analysis", exploratoryDataAnalysis.app)
app.add_app("About Machine Learning Model", aboutmlmodel.app)
app.add_app("Insight Dashboard", dashboard.app)
app.run()

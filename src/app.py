from imghdr import what
import streamlit as st
import apps.xmlversion as xmlversion
import apps.whatitdoes as whatitdoes
import apps.relaxng as relaxng
import apps.xsd as xsd
import apps.dtdversion as dtdversion
import apps.exploratoryDataAnalysis as exploratoryDataAnalysis
import apps.aboutmlmodel as aboutmlmodel
import apps.docs as docs
import apps.userofdb as userofdb
import apps.interactiveapp as interactiveapp
from app import about_dataset
from multiapp import MultiApp
# import dashboard

PAGES = {
    "Interactive App": interactiveapp,
    "What Recipe Generator does?": whatitdoes,
    "About Dataset": about_dataset,
    "XML Version of Data": xmlversion,
    "DTD Version of Data": dtdversion,
    "RELAXNG Version": relaxng,
    "XSD Version": xsd,
    "EDA": exploratoryDataAnalysis,
    "About Machine Learning Model": aboutmlmodel,
    "Use of Database": userofdb,
    # "Dashboard": dashboard,
    "Documentation": docs
}
# st.title("Recipe Generator App")

# add_selectbox = st.sidebar.selectbox(
#     "How would you like to be contacted?",
#     ("Email", "Home phone", "Mobile phone")
# )

# selection = st.sidebar.radio("Go to", list(PAGES.keys()))
# page = PAGES[selection]
# page.app()

app = MultiApp()
app.add("Home", about_dataset.app)
# app.add("Data", data.app)
app.run()
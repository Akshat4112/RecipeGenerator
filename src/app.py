from imghdr import what
import streamlit as st
import about_dataset
import xmlversion
import whatitdoes
import relaxng
import xsd
import dtdversion
import exploratoryDataAnalysis
import aboutmlmodel
import docs
import userofdb
import interactiveapp
import dashboard

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
    "Dashboard": dashboard,
    "Documentation": docs
}
st.title("Recipe Generator App")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()


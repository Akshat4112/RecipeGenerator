from imghdr import what
import streamlit as st
# import xmlversion
# import whatitdoes
# import relaxng
# import xsd
# import dtdversion
# import exploratoryDataAnalysis
# import aboutmlmodel
# import docs
# import userofdb
# import interactiveapp
from apps import about_dataset, aboutmlmodel, dashboard, docs, dtdversion, exploratoryDataAnalysis, interactiveapp, relaxng, userofdb, whatitdoes, xmlversion, xsd
from multiapp import MultiApp
# import dashboard
st.title("Recipe Generator App")
app = MultiApp()
app.add_app("HomePage", interactiveapp.app)
app.add_app("What Recipe Genrator Does?", whatitdoes.app)
app.add_app("About Dataset", about_dataset.app)
app.add_app("XML Version of data", xmlversion.app)
app.add_app("DTD Version of data", dtdversion.app)
app.add_app("XSD Verion of data", xsd.app)
app.add_app("RELAXNG Version of data", relaxng.app)
app.add_app("Exploratory Data Analysis", exploratoryDataAnalysis.app)
app.add_app("About Machine Learning Model", aboutmlmodel.app)
app.add_app("Insight Dashboard", dashboard.app)
app.add_app("Documentation", docs.app)
# app.add("Data", data.app)
app.run()


# add_selectbox = st.sidebar.selectbox(
#     "How would you like to be contacted?",
#     ("Email", "Home phone", "Mobile phone")
# )

# selection = st.sidebar.radio("Go to", list(PAGES.keys()))
# page = PAGES[selection]
# page.app()


import streamlit as st
def app():
    st.title("About the Dataset")
    st.subheader("Context")
    st.markdown("This dataset contains 12190 german recipes with metadata crawled from chefkoch.de*.")

    st.subheader("Content")
    st.markdown("Each json document contains the following fields:")

    st.markdown("Ingredients: the ingredients of the recipe as array")
    st.markdown("Instructions: the instructions as free text")
    st.markdown("Name: the name of the recipe")
    st.markdown("Url: the source url")
    st.markdown("Day: the day where the recipe was created")
    st.markdown("Month: the month where the recipe was created")
    st.markdown("Year: the year where the recipe was created")
    st.markdown("Weekday: the weekday where the recipe was created")
    st.markdown("Projects using this dataset")
    st.markdown("Learn to identify ingredients with neural networks")
    st.subheader("Acknowledgements")
    st.markdown("The data is for research purposes only and belongs to www.chefkoch.de.")
    st.markdown("The data has been collected with the help of https://github.com/TobiasPleyer/chefkoch")

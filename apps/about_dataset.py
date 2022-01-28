import streamlit as st
def app():
    st.subheader("About the Dataset")
    # st.subheader("Context")
    # st.write("This dataset contains 12190 german recipes with metadata crawled from chefkoch.de*.")

    # st.subheader("Content")
    # st.write("Each json document contains the following fields:")
    # st.write("Ingredients: the ingredients of the recipe as array")
    # st.write("Instructions: the instructions as free text")
    # st.write("Name: the name of the recipe")
    # st.write("Url: the source url")
    # st.write("Day: the day where the recipe was created")
    # st.write("Month: the month where the recipe was created")
    # st.write("Year: the year where the recipe was created")
    # st.markdown("Weekday: the weekday where the recipe was created")
    # st.write("Projects using this dataset")
    # st.write("Learn to identify ingredients with neural networks")
    # st.subheader("Acknowledgements")
    # st.write("The data is for research purposes only and belongs to www.chefkoch.de.")
    # st.write("The data has been collected with the help of https://github.com/TobiasPleyer/chefkoch")
    
    st.write('''
    This dataset contains 12190 german recipes with metadata crawled from chefkoch.de*. \n
    Each json document contains the following fields: \n
    Ingredients: the ingredients of the recipe as array \n
    Instructions: the instructions as free text \n
    Name: the name of the recipe \n
    Url: the source url \n
    Day: the day where the recipe was created \n
    Month: the month where the recipe was created \n
    Year: the year where the recipe was created \n
    Weekday: the weekday where the recipe was created \n
    
    Acknowledgements \n
    The data is for research purposes only and belongs to www.chefkoch.de. \n
    The data has been collected with the help of https://github.com/TobiasPleyer/chefkoch ''')
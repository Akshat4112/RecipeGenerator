import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)


def explore_data():
    df = pd.read_csv("data/processed/recipes_csv.csv")
    df = df.drop(columns=['index', 'Unnamed: 0'])
    return df


def app():
    st.title("EDA on dataset")
    data = explore_data()
    if st.checkbox("Show Dataset"):
        if st.button("Head"):
            st.write(data.head())
        elif st.button("Tail"):
            st.write(data.tail())
        else:
            st.write(data.head(2))

    if st.checkbox("Show All Dataset"):
        st.write(data)

    if st.checkbox("Show Column Names"):
        st.write(data.columns)

    data_dim = st.radio(
        'What Dimension Do You Want to Show', ('Rows', 'Columns'))
    if data_dim == 'Rows':
        st.text("Showing Length of Rows")
        st.write(len(data))
    if data_dim == 'Columns':
        st.text("Showing Length of Columns")
        st.write(data.shape[1])

    species_option = st.selectbox(
        'Select Columns', ('Url', 'Instructions', 'Ingredients', 'Day', 'Name', 'Year', 'Month', 'Weekday'))
    if species_option in data.columns:
        st.write(data[species_option])
    else:
        st.write("Select A Column")

    if st.checkbox("Show Year Distribution"):
        fig, ax = plt.subplots(figsize=(5, 5))
        data.Year.value_counts().plot(kind='bar', ax=ax)
        st.pyplot(fig)

    if st.checkbox("Show Month Distribution"):
        fig, ax = plt.subplots(figsize=(5, 5))
        data.Month.value_counts().plot(kind='bar', ax=ax)
        st.pyplot(fig)

    if st.checkbox("Show Weekday Distribution"):
        fig, ax = plt.subplots(figsize=(5, 5))
        data.Weekday.value_counts().plot(kind='bar', ax=ax)
        st.pyplot(fig)

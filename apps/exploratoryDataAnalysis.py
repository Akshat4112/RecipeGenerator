from prometheus_client import Counter
import streamlit as st
import pandas as pd
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)
# @st.cache(persist=True)


def explore_data():
    df = pd.read_csv("data/processed/recipes_csv.csv")
    df = df.drop(columns=['index', 'Unnamed: 0'])
    return df

# Function to show EDA on the Dataset on the dashboard


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
        data = explore_data()
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
    data = explore_data()
    if species_option == 'Url':
        st.write(data['Url'])
    elif species_option == 'Instructions':
        st.write(data['Instructions'])
    elif species_option == 'Ingredients':
        st.write(data['Ingredients'])
    elif species_option == 'Day':
        st.write(data['Day'])
    elif species_option == 'Name':
        st.write(data['Name'])
    elif species_option == 'Year':
        st.write(data['Year'])
    elif species_option == 'Month':
        st.write(data['Month'])
    elif species_option == 'Weekday':
        st.write(data['Weekday'])
    else:
        st.write("Select A Column")

    if st.checkbox("Show Year Distribution"):
        st.write(data.Year.value_counts().plot(kind='bar', figsize=(5, 5)))
        st.pyplot()

    if st.checkbox("Show Month Distribution"):
        st.write(data.Month.value_counts().plot(kind='bar', figsize=(5, 5)))
        st.pyplot()

    if st.checkbox("Show Weekday Distribution"):
        st.write(data.Weekday.value_counts().plot(kind='bar', figsize=(5, 5)))
        st.pyplot()

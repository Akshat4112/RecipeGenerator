import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# @st.cache(persist=True)
def explore_data():
    df = pd.read_csv("../data/processed/recipes_csv.csv")
    df = df.drop(columns=['index','Unnamed: 0'])
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
        data = explore_data()
        st.write(data)

    if st.checkbox("Show Column Names"):
        st.write(data.columns)

    data_dim = st.radio('What Dimension Do You Want to Show',('Rows','Columns'))
    if data_dim == 'Rows':
        st.text("Showing Length of Rows")
        st.write(len(data))
    if data_dim == 'Columns':
        st.text("Showing Length of Columns")
        st.write(data.shape[1])

    # Show Summary of Dataset
    if st.checkbox("Show Summary of Dataset"):
        st.write(data.describe())

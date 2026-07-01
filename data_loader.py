import pandas as pd
import streamlit as st


@st.cache_data
def load_recipes() -> pd.DataFrame:
    df = pd.read_csv("data/processed/recipes_csv.csv")
    df = df.drop(columns=["index", "Unnamed: 0"], errors="ignore")
    return df

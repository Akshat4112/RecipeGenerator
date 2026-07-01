import streamlit as st
import pandas as pd
from collections import Counter

from db import get_connection


def app():
    st.markdown("Data Insight Dashboard")

    try:
        with get_connection() as conn:
            df = pd.read_sql_query("SELECT * FROM history", conn)
    except Exception as e:
        st.error(f"Fehler beim Laden der Daten: {e}")
        return

    if df.empty:
        st.info("Noch keine Daten vorhanden.")
        return

    top_items = Counter(df["input_text"]).most_common(10)
    top_df = pd.DataFrame(top_items, columns=["Ingredient", "Count"])

    left_column, right_column = st.columns(2)
    with left_column:
        st.text("Top 10 search items are:")
        st.dataframe(top_df)
    with right_column:
        st.bar_chart(top_df.set_index("Ingredient"))

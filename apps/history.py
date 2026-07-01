import pandas as pd
import streamlit as st

from db import get_connection


def app() -> None:
    st.subheader("Rezeptverlauf")

    try:
        with get_connection() as conn:
            df = pd.read_sql_query(
                "SELECT * FROM history ORDER BY date DESC", conn
            )
    except Exception as e:
        st.error(f"Fehler beim Laden: {e}")
        return

    if df.empty:
        st.info("Noch keine Rezepte generiert.")
        return

    search = st.text_input("Verlauf durchsuchen")
    if search.strip():
        df = df[df["input_text"].str.contains(search, case=False, na=False)]

    st.write(f"**{len(df)}** Einträge")

    for _, row in df.iterrows():
        label = f"[{row['date'][:16]}] {row['input_text']}"
        with st.expander(label):
            st.write(row["generated_text"])

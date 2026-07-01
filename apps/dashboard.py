from collections import Counter

import pandas as pd
import streamlit as st

from db import get_connection


def app() -> None:
    st.subheader("Analyse-Dashboard")

    try:
        with get_connection() as conn:
            df = pd.read_sql_query("SELECT * FROM history", conn)
    except Exception as e:
        st.error(f"Fehler beim Laden der Daten: {e}")
        return

    if df.empty:
        st.info("Noch keine Daten vorhanden.")
        return

    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Von", value=df["date"].min())
    with col2:
        end_date = st.date_input("Bis", value=df["date"].max())

    mask = (df["date"] >= pd.Timestamp(start_date)) & (df["date"] <= pd.Timestamp(end_date) + pd.Timedelta(days=1))
    filtered = df.loc[mask]

    st.write(f"**{len(filtered)}** Generierungen im gewählten Zeitraum")

    if filtered.empty:
        st.info("Keine Daten im gewählten Zeitraum.")
        return

    top_items = Counter(filtered["input_text"]).most_common(10)
    top_df = pd.DataFrame(top_items, columns=["Zutat", "Anzahl"])

    left_column, right_column = st.columns(2)
    with left_column:
        st.text("Top 10 gesuchte Zutaten:")
        st.dataframe(top_df)
    with right_column:
        st.bar_chart(top_df.set_index("Zutat"))

    st.download_button(
        "CSV exportieren",
        filtered.to_csv(index=False),
        "verlauf.csv",
        "text/csv",
    )

import altair as alt
import streamlit as st

from data_loader import load_recipes


def app() -> None:
    st.title("Explorative Datenanalyse")
    data = load_recipes()

    if st.checkbox("Datensatz anzeigen"):
        if st.button("Anfang"):
            st.write(data.head())
        elif st.button("Ende"):
            st.write(data.tail())
        else:
            st.write(data.head(2))

    if st.checkbox("Gesamten Datensatz anzeigen"):
        st.write(data)

    if st.checkbox("Spaltennamen anzeigen"):
        st.write(data.columns)

    data_dim = st.radio(
        "Welche Dimension anzeigen?", ("Zeilen", "Spalten"))
    if data_dim == "Zeilen":
        st.text("Anzahl der Zeilen")
        st.write(len(data))
    if data_dim == "Spalten":
        st.text("Anzahl der Spalten")
        st.write(data.shape[1])

    species_option = st.selectbox(
        "Spalte auswählen",
        ("Url", "Instructions", "Ingredients", "Day", "Name", "Year", "Month", "Weekday"),
    )
    if species_option in data.columns:
        st.write(data[species_option])
    else:
        st.write("Spalte auswählen")

    if st.checkbox("Jahresverteilung anzeigen"):
        year_counts = data["Year"].value_counts().reset_index()
        year_counts.columns = ["Jahr", "Anzahl"]
        chart = alt.Chart(year_counts).mark_bar().encode(
            x=alt.X("Jahr:N", sort="-y"),
            y="Anzahl:Q",
            tooltip=["Jahr", "Anzahl"],
        )
        st.altair_chart(chart, use_container_width=True)

    if st.checkbox("Monatsverteilung anzeigen"):
        month_counts = data["Month"].value_counts().reset_index()
        month_counts.columns = ["Monat", "Anzahl"]
        chart = alt.Chart(month_counts).mark_bar().encode(
            x=alt.X("Monat:N", sort="-y"),
            y="Anzahl:Q",
            tooltip=["Monat", "Anzahl"],
        )
        st.altair_chart(chart, use_container_width=True)

    if st.checkbox("Wochentagsverteilung anzeigen"):
        weekday_counts = data["Weekday"].value_counts().reset_index()
        weekday_counts.columns = ["Wochentag", "Anzahl"]
        chart = alt.Chart(weekday_counts).mark_bar().encode(
            x=alt.X("Wochentag:N", sort="-y"),
            y="Anzahl:Q",
            tooltip=["Wochentag", "Anzahl"],
        )
        st.altair_chart(chart, use_container_width=True)

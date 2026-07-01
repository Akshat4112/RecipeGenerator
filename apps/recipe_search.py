import streamlit as st

from data_loader import load_recipes

RECIPES_PER_PAGE = 20


def app() -> None:
    st.subheader("Rezeptsuche")

    data = load_recipes()

    search = st.text_input("Rezept oder Zutat suchen")

    col1, col2 = st.columns(2)
    with col1:
        years = ["Alle"] + sorted(data["Year"].dropna().unique().tolist())
        year = st.selectbox("Jahr", years)
    with col2:
        months = ["Alle"] + sorted(data["Month"].dropna().unique().tolist())
        month = st.selectbox("Monat", months)

    filtered = data
    if search.strip():
        mask = (
            filtered["Name"].str.contains(search, case=False, na=False)
            | filtered["Ingredients"].str.contains(search, case=False, na=False)
        )
        filtered = filtered[mask]
    if year != "Alle":
        filtered = filtered[filtered["Year"] == year]
    if month != "Alle":
        filtered = filtered[filtered["Month"] == month]

    st.write(f"**{len(filtered)}** Rezepte gefunden")

    if filtered.empty:
        st.info("Keine Rezepte gefunden.")
        return

    max_pages = max(1, (len(filtered) - 1) // RECIPES_PER_PAGE + 1)
    page = st.number_input("Seite", min_value=1, max_value=max_pages, value=1)
    start = (page - 1) * RECIPES_PER_PAGE
    page_data = filtered.iloc[start:start + RECIPES_PER_PAGE]

    for _, row in page_data.iterrows():
        with st.expander(f"{row['Name']} ({row.get('Year', '')})"):
            st.markdown(f"**Zutaten:** {row['Ingredients']}")
            st.markdown(f"**Zubereitung:** {row['Instructions']}")
            st.caption(f"Quelle: {row['Url']}")

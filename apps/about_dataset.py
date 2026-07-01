import streamlit as st


def app() -> None:
    st.subheader("Über den Datensatz")
    st.write("""
    Dieser Datensatz enthält 12.190 deutsche Rezepte mit Metadaten, die von chefkoch.de gecrawlt wurden.

    Jedes Dokument enthält folgende Felder:
    - **Ingredients:** Die Zutaten des Rezepts als Liste
    - **Instructions:** Die Zubereitungsanweisungen als Freitext
    - **Name:** Der Name des Rezepts
    - **Url:** Die Quell-URL
    - **Day:** Der Tag, an dem das Rezept erstellt wurde
    - **Month:** Der Monat der Erstellung
    - **Year:** Das Jahr der Erstellung
    - **Weekday:** Der Wochentag der Erstellung

    **Hinweis:** Die Daten dienen ausschließlich Forschungszwecken und gehören www.chefkoch.de.
    Die Daten wurden mit Hilfe von https://github.com/TobiasPleyer/chefkoch gesammelt.
    """)

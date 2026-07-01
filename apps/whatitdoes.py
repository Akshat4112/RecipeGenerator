import streamlit as st


def app() -> None:
    st.subheader("Was macht der Rezeptgenerator?")
    st.write(
        "Willkommen! Wir freuen uns, dass Sie unseren deutschen Rezeptgenerator besuchen. "
        "Der Rezeptgenerator akzeptiert eine oder mehrere Zutaten als Texteingabe und "
        "generiert daraus ein Rezept mit Zubereitungsanweisungen. "
        "Mit dem Rezeptgenerator möchten wir Ihnen helfen, neue Rezepte zu entdecken, "
        "mit denen Sie Lebensmittelreste verwerten können."
    )

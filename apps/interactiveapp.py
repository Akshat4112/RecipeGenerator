from datetime import datetime

import streamlit as st

from db import get_connection
from model import generate_recipe


def app() -> None:
    st.subheader("Willkommen beim Rezeptgenerator")
    st.text("Text Technology Projekt, Klasse 21-22")
    st.text("Eingereicht bei: Kerstin Jung")
    st.text("Eingereicht von: Silvia Cunico, Akshat Gupta")

    with st.sidebar.expander("Einstellungen"):
        temperature = st.slider("Temperatur", 0.1, 2.0, 1.0, 0.1,
                                help="Höhere Werte = kreativer, niedrigere = konservativer")
        max_length = st.slider("Maximale Länge", 50, 500, 200, 50,
                               help="Maximale Anzahl generierter Tokens")
        top_p = st.slider("Top-p", 0.1, 1.0, 0.9, 0.05,
                          help="Nucleus Sampling: kleinere Werte = fokussierter")

    text_inp = st.text_input("Zutaten eingeben", max_chars=500)

    if st.button("Generieren"):
        if not text_inp.strip():
            st.warning("Bitte geben Sie Zutaten ein.")
            return

        with st.spinner("Rezept wird generiert..."):
            try:
                model_output = generate_recipe(
                    text_inp,
                    temperature=temperature,
                    max_length=max_length,
                    top_p=top_p,
                )
            except Exception as e:
                st.error(f"Fehler bei der Rezeptgenerierung: {e}")
                return

        st.success("Da ist dein Rezept!")
        st.write(model_output)

        try:
            with get_connection() as conn:
                conn.execute(
                    "INSERT INTO history (input_text, generated_text, date) VALUES (?, ?, ?)",
                    (text_inp, model_output, datetime.now().isoformat()),
                )
                conn.commit()
        except Exception as e:
            st.error(f"Fehler beim Speichern: {e}")

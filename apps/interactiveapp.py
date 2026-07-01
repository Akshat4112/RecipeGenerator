import streamlit as st
from datetime import datetime

from db import get_connection
from model import generate_recipe


def app():
    st.text("Text Technology Project, Class of 21-22")
    st.text("Submitted to: Kerstin Jung")
    st.text("Submitted by: Silvia Cunico, Akshat Gupta")
    text_inp = st.text_input("Zutaten eingeben")

    if st.button("Generate"):
        if not text_inp.strip():
            st.warning("Bitte geben Sie Zutaten ein.")
            return

        with st.spinner("Rezept wird generiert..."):
            try:
                model_output = generate_recipe(text_inp)
            except Exception as e:
                st.error(f"Fehler bei der Rezeptgenerierung: {e}")
                return

        st.warning("Da ist dein Rezept!")
        st.success(model_output)

        try:
            with get_connection() as conn:
                conn.execute(
                    "INSERT INTO history (input_text, model, date) VALUES (?, ?, ?)",
                    (text_inp, model_output, datetime.now().isoformat()),
                )
                conn.commit()
        except Exception as e:
            st.error(f"Fehler beim Speichern: {e}")

import streamlit as st


def app() -> None:
    st.subheader("ML-Modell: GPT-2 Architektur")
    st.image("./images/gpt2.png")
    st.markdown(
        "GPT-2 ist ein großes transformerbasiertes Sprachmodell mit 1,5 Milliarden Parametern, "
        "das auf einem Datensatz von 8 Millionen Webseiten trainiert wurde. "
        "GPT-2 wird mit einem einfachen Ziel trainiert: das nächste Wort vorherzusagen, "
        "basierend auf allen vorherigen Wörtern in einem Text. "
        "Wir verwenden eine deutsche Variante (german-gpt2), die auf deutschen Texten vortrainiert wurde."
    )

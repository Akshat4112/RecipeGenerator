import streamlit as st
# Function which describes about GPT2 Machine Learning Model used? and how it is being trained?


def app():
    st.subheader("ML Model: GPT2 Architecture")
    st.image("./images/gpt2.png")
    st.markdown("GPT-2 is a large transformer-based language model with 1.5 billion parameters, trained on a dataset of 8 million web pages. GPT-2 is trained with a simple objective: predict the next word, given all of the previous words within some text.")

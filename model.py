import os
import streamlit as st
from transformers import pipeline
from config import MODEL_NAME, LOCAL_MODEL_PATH, MAX_LENGTH


@st.cache_resource
def load_model():
    model_path = LOCAL_MODEL_PATH if os.path.isdir(LOCAL_MODEL_PATH) else MODEL_NAME
    return pipeline(
        "text-generation",
        model=model_path,
        tokenizer=MODEL_NAME,
    )


def generate_recipe(ingredients):
    chef = load_model()
    result = chef(ingredients, max_length=MAX_LENGTH, num_return_sequences=1)
    return result[0]["generated_text"]

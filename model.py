import os

import streamlit as st
from transformers import pipeline as hf_pipeline

from config import LOCAL_MODEL_PATH, MAX_LENGTH, MODEL_NAME

PROMPT_TEMPLATE = "Zutaten: {ingredients}\n\nZubereitung:"


@st.cache_resource
def load_model():
    model_path = LOCAL_MODEL_PATH if os.path.isdir(LOCAL_MODEL_PATH) else MODEL_NAME
    return hf_pipeline(
        "text-generation",
        model=model_path,
        tokenizer=MODEL_NAME,
    )


def generate_recipe(
    ingredients: str,
    temperature: float = 1.0,
    max_length: int = MAX_LENGTH,
    top_p: float = 0.9,
) -> str:
    prompt = PROMPT_TEMPLATE.format(ingredients=ingredients)
    chef = load_model()
    result = chef(
        prompt,
        max_length=max_length,
        num_return_sequences=1,
        temperature=temperature,
        top_p=top_p,
        do_sample=True,
    )
    return result[0]["generated_text"]

import os
import sys

from flask import Flask, json, request
from transformers import pipeline

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import LOCAL_MODEL_PATH, MAX_LENGTH, MODEL_NAME

app = Flask(__name__)

model_path = LOCAL_MODEL_PATH if os.path.isdir(LOCAL_MODEL_PATH) else MODEL_NAME
chef = pipeline("text-generation", model=model_path, tokenizer=MODEL_NAME)


@app.route("/")
def test():
    return "Recipe Generator API"


@app.route("/predict_text", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("text", "")
    if not text.strip():
        return json.dumps({"error": "No input text provided"}), 400
    result = chef(text, max_length=MAX_LENGTH, num_return_sequences=1)
    return json.dumps({"prediction": result})


if __name__ == "__main__":
    app.run(port=5001)

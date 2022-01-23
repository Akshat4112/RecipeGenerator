# pyright: reportUnboundVariable=false
from typing import Counter
from flask import Flask, request, jsonify,json
import pandas as pd
import numpy as np
# import pickle
# from pathlib import Path    
# from datetime import datetime
# import json
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder
from transformers import pipeline

app = Flask(__name__)

# load the model from disk
chef = pipeline('text-generation',model='./gpt2-gerchef', tokenizer='anonymous-german-nlp/german-gpt2')

@app.route('/')
def test():
    return "Test API"

@app.route('/predict_text', methods=["POST"])
def predict():
    #Take text input
    result = chef('Zuerst Hähnchen') 
    result = result[0]['generated_text']
    print(result)
    return json.dumps({"prediction": result})

if __name__== '__main__':
    app.run(port=5001)

#ssh -i "textech.pem" ubuntu@ec2-3-144-203-238.us-east-2.compute.amazonaws.com
#ec2-3-144-203-238.us-east-2.compute.amazonaws.com
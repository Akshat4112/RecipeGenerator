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

app = Flask(__name__)

# load the model from disk
#Loading all models
# model = pickle.load(open('modelpath', 'rb'))  #modelpath will be there

@app.route('/')
def test():
    return "Test API"

@app.route('/predict_file', methods=["POST"])
def predict_file():
    print("prediction")
    # prediction = model.predict(df_filtered)
    # return json.dumps(result)

if __name__== '__main__':
    app.run(port=5001)

#ssh -i "ubuntu18_vent_team.pem" ubuntu@ec2-13-127-11-176.ap-south-1.compute.amazonaws.com
#ec2-3-138-139-136.us-east-2.compute.amazonaws.com
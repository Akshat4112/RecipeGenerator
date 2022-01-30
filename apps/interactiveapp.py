import streamlit as st
import os
import time
import requests
import json
import ast

def app():
    st.text("Text Technology Project, Class of 21-22")
    st.text("Submitted to: Kerstin Jung")
    st.text("Submitted by: Silvia Cunico, Akshat Gupta")
    text_inp = st.text_input("Enter Ingredients")
    
    if(st.button("Generate")):
        #API Call on text
        url = "http://3.20.227.146:5001/predict_text"
        payload = json.dumps({"text": text_inp})
        headers = {'Content-Type': 'application/json'}
        response = requests.request("POST", url, headers=headers, data=payload)
        res =  response.text
        print(type(res))
        res= ast.literal_eval(res)
        progress = st.progress(0)
        for i in range(100):
            time.sleep(0.1)
            progress.progress(i+1)        
        
        st.warning("Da ist deine Rezepte!")
        st.success(res["prediction"][0]["generated_text"])
import streamlit as st
import os
import time
import requests
import json
import ast
import sqlite3
from datetime import date, datetime
now = datetime.now()

# Function to create the connection


def create_connection(dbfile):
    conn = None
    try:
        conn = sqlite3.connect(dbfile)
    except Exception as e:
        print(e)

    return conn

# Function to create the Interactive app, Homepage


def app():
    st.text("Text Technology Project, Class of 21-22")
    st.text("Submitted to: Kerstin Jung")
    st.text("Submitted by: Silvia Cunico, Akshat Gupta")
    text_inp = st.text_input("Zutaten eingeben")

    if(st.button("Generate")):
        # API Call on text, API is deployed on AWS Instance
        url = "http://3.20.227.146:5001/predict_text"
        payload = json.dumps({"text": text_inp})
        headers = {'Content-Type': 'application/json'}
        response = requests.request("POST", url, headers=headers, data=payload)
        res = response.text
        res = ast.literal_eval(res)
        progress = st.progress(0)
        for i in range(100):
            time.sleep(0.1)
            progress.progress(i+1)

        st.warning("Da ist deine Rezepte!")
        st.success(res["prediction"][0]["generated_text"])
        model_output = res["prediction"][0]["generated_text"]

        # Creating a entry in DB
        database = "textechdb781"
        conn = create_connection(database)
        c = conn.cursor()
        c.execute('''INSERT INTO history (input_text, model, date) VALUES (?,?,?)''',
                  (text_inp, model_output, now))
        c.execute('''SELECT * FROM history''')
        rows = c.fetchall()
        for row in rows:
            print(row)
        conn.commit()

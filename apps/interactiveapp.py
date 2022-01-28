import streamlit as st
import os
import time

def app():
    st.text("Text Technology Project, Class of 21-22")
    st.text("Submitted to: Kerstin Jung")
    st.text("Submitted by: Silvia Cunico, Akshat Gupta")
    text = st.text_input("Enter Ingredients")

    if(st.button("Generate")):
        progress = st.progress(0)
        for i in range(100):
            time.sleep(0.1)
            progress.progress(i+1)        
        #API Call on text
        st.warning("Here is your Recipe! ")
        text = "zwiebeln mit der Sauce anbraten, mit der Gurkenhälften und einem fein gehackten Käse bestreuen und etwa 6-8 Stunden schmoren lassen.Nach Ende dieser Zeit die Pilze aus dem Glas vierteln und mit dem restlichen"
        st.success(text)
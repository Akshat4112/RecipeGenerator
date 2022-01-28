import streamlit as st
import os
import time

def app():
    st.text("Text Technology Project, Class of 21-22")
    st.text("Submitted to: Kerstin Jung")
    st.text("Submitted by: Silvia Cunico, Akshat Gupta")
    st.text_input("Enter Ingredients")

    if(st.button("Generate")):
        st.text("Generating Recipe...")
        gif_runner = st.image("../images/6.gif")
        time.sleep(5)
        gif_runner.empty()
        #API CALL
        text = "zwiebeln mit der Sauce anbraten, mit der Gurkenhälften und einem fein gehackten Käse bestreuen und etwa 6-8 Stunden schmoren lassen.Nach Ende dieser Zeit die Pilze aus dem Glas vierteln und mit dem restlichen"
        st.success(text)
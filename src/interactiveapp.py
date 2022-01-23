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
        text = "Potato, Tomato, and Lemon"
        st.success(text)
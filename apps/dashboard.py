import streamlit as st
import sqlite3
import pandas as pd

# conn = sqlite3.connect('textechdb781')
# c = conn.cursor()
# c.execute('''SELECT * FROM history''')
# conn.commit()
# df = pd.DataFrame(c.fetchall(), columns=['id','input_text', 'model', 'date'])


def app():
    st.markdown("Data Insight Dashboard")
    left_column, right_column = st.columns(2)
    # You can use a column just like st.sidebar:
    with left_column:
        start_date = st.date_input("Start Date:")
        end_date = st.date_input("End Date:")

    # Or even better, call Streamlit functions inside a "with" block:
    with right_column:
        print("Chart")
        

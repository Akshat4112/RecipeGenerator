from pyparsing import col
import streamlit as st
import sqlite3
import pandas as pd
import sqlite3
from collections import Counter

# Function to create a dabase connection


def create_connection(dbfile):
    conn = None
    try:
        conn = sqlite3.connect(dbfile)
    except Exception as e:
        print(e)

    return conn


# code to fetch data from database and create a dataframe out of it.
database = "textechdb781"
conn = create_connection(database)
c = conn.cursor()
c.execute('''SELECT * FROM history''')
df = pd.DataFrame(c.fetchall(), columns=['id', 'input_text', 'model', 'date'])
print(df.tail())

# Code block to get top 10 items out of database
top_10 = df['input_text']
top_10_item = []
for item in df['input_text']:
    top_10_item.append(item)
top_10_item = Counter(top_10_item)
top_10_item = dict(top_10_item)

top_10_dict = pd.DataFrame.from_dict(top_10_item, orient='index')
top_10_dict.columns = ['name']

# Function to get data on insight dashboard.


def app():
    st.markdown("Data Insight Dashboard")
    left_column, right_column = st.columns(2)
    # You can use a column just like st.sidebar:
    with left_column:
        st.text("Top 10 search items are: ")
        st.dataframe(top_10_dict[:10])
        print("Chart")

    # Or even better, call Streamlit functions inside a "with" block:
    with right_column:
        print("Draw a Chart")
        print(top_10_dict.name.value_counts())

# import streamlit as st
# import sqlite3
# import pandas as pd
# conn = sqlite3.connect('textechdb781')
# c = conn.cursor()
# c.execute('''SELECT * FROM history''')
# conn.commit()
# df = pd.DataFrame(c.fetchall(), columns=['id','input_text', 'model', 'date'])


# def app():
#     st.title("Data Insight Dashboard")
#     left_column, right_column = st.columns(2)
#     # You can use a column just like st.sidebar:
#     left_column.button('Press me!')

#     # Or even better, call Streamlit functions inside a "with" block:
#     with right_column:
#         chosen = st.radio(
#             'Sorting hat',
#             ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
#         st.write(f"You are in {chosen} house!")

# app()    
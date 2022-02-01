import sqlite3
import pandas as pd
from datetime import datetime
conn = sqlite3.connect('textechdb781')
c = conn.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS history
          ([id] INTEGER PRIMARY KEY AUTOINCREMENT, [input_text] TEXT, [model] TEXT, [date] TEXT)
          ''')

text_inp = 'onion'
model_output = 'this is onion'
now = datetime.now()
c.execute('''INSERT INTO history (input_text, model, date) VALUES(?,?,?)''',(text_inp, model_output, now ))
c.execute('''SELECT * FROM history''')
conn.commit()

df = pd.DataFrame(c.fetchall(), columns=['id','input_text', 'model', 'date'])
print(df)
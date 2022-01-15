import sqlite3
import pandas as pd
conn = sqlite3.connect('textechdb4')
c = conn.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS history
          ([id] INTEGER PRIMARY KEY, [input_text] TEXT, [model] TEXT, [date] TEXT)
          ''')


c.execute('''
          INSERT INTO history (id, input_text, model, date)
                VALUES
                (1,'potato', 'mesh', '15-01-2022 Saturday'),
                (2,'tomato', 'mesh', '16-01-2022 Saturday')
          ''')

c.execute('''SELECT * FROM history
''')
conn.commit()
df = pd.DataFrame(c.fetchall(), columns=['id','input_text', 'model', 'date'])
print(df)
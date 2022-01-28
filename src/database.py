import sqlite3
import pandas as pd
conn = sqlite3.connect('textechdb781')
c = conn.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS history
          ([id] INTEGER PRIMARY KEY, [input_text] TEXT, [model] TEXT, [date] TEXT)
          ''')


c.execute('''
          INSERT INTO history (id, input_text, model, date)
                VALUES
                (1,'zwiebeln', 'zwiebeln mit der Sauce anbraten mit der Gurkenhälften und einem fein gehackten Käse bestreuen und etwa 6-8 Stunden schmoren lassen.Nach Ende dieser Zeit die Pilze aus dem Glas vierteln und mit dem restlichen', '15-01-2022 Saturday'),
                (2,'Die Nudeln Kochen Fleisch anbraten', 'Die Nudeln Kochen Fleisch anbraten und zusammen mit den Paprika in die Sauce rühren. Mit Salz Pfeffer Paprika Koriander Ingwer Koriander Knoblauch und Paprikapulver abschmecken', '16-01-2022 Sunday'),
                (3,'Zuerst Hähnchen', 'Zuerst Hähnchenbrustfilets aufschneiden den Fisch umdrehen und in ca. 4 x 4 cm große Würfel schneiden.Nun werden Hähnchenbrustfilets bei 180°C in den vorgeheizten Backofen gestellt. Sollte der', '16-01-2022 Sunday'),
                (4,'Kartoffelpuffer', 'Kartoffelpuffer nach Packungsanweisung gar kochen.  Das Suppengemüse 2 große Möhren ein Stück Sellerie eine halbe Stange Porree - das Weiße und die Zwiebel in gleich große Würfelchen schneiden de', '16-01-2022 Sunday'),
                (5,'Kohlrabi schälen und klein würfeln.', 'Kartoffeln schälen, waschen, vierteln und in kochendem Salzwasser ca. 12 min gar kochen lassen.Den Spargel schälen und rüsten, mit Kräutern und Oliven zupfen.Die Zutaten für den Teig mischen und kurz mit ver', '16-01-2022 Sunday')
          ''')

c.execute('''SELECT * FROM history
''')
conn.commit()
df = pd.DataFrame(c.fetchall(), columns=['id','input_text', 'model', 'date'])
print(df)
import streamlit as st
def app():
  st.subheader("XML for the Dataset")
  code  = ''' <?xml version='1.0' encoding='utf-8'?>
  <data>
    <row>
      <index>0</index>
      <Url>https://www.chefkoch.de/rezepte/185441079701305/</Url>
      <Instructions>Die Eier hart kochen. Dann pellen und mit einem Eierschneider in Scheiben schneiden. Den Reis halbgar kochen und zur Seite stellen. Die Wurst (Kolbász) in dünne Scheiben schneiden.Den Knoblauch abziehen und fein würfeln. Die Zwiebel schälen, fein hacken und in etwas Fett glasig braten. Knoblauch und Hackfleisch dazu geben und so lange braten, bis das Hackfleisch schön krümelig wird. Den eigenen Saft nicht ganz verkochen lassen. Die Fleischmasse mit Salz, Pfeffer und Paprikapulver würzen.Das Sauerkraut kurz durchspülen, ausdrücken und abtropfen lassen (damit es nicht zu sauer wird). Das Sauerkraut in einen Topf geben und mit dem Kümmel und den Lorbeerblättern vermischen. Ca. 30 Minuten unter Zugabe von wenig Wasser bei niedriger Stufe dünsten.Eine feuerfeste Form mit etwas Öl einfetten und den Boden dünn mit Sauerkraut belegen. Darauf Kolbász und die Hälfte der in Scheiben geschnittene Eier verteilen, dann eine weitere dünne Schicht Sauerkraut drüber legen. Mit 1 Becher Schmand bedecken. Nun das Hackfleisch mit dem Reis mischen und auf der Sauerkrautschicht gleichmäßig verteilen. Mit der zweiten Hälfte der Eier belegen und die dritte Schicht Sauerkraut oben drauf verteilen. Wenn noch Zutaten (Hackfleisch-Reis-Masse und Sauerkraut) übrig sind, kann man diese Schichten weiter so legen. Ganz oben kommt eine Schicht Sauerkraut. Auf diese letzte Schicht verteilt man noch den Rest vom Schmand (sollte reichlich sein). Den Speck in dünne Scheiben schneiden und damit alles abdecken. Mit etwas Öl besprenkeln. Die Form mit einem Deckel verschließend.Im vorgeheizten Backofen bei 175°C ober-/Unterhitze gut 1 Std. garen.Ganz frische Baguettebrötchen oder Weißbrot schmeckt am allerbesten dazu. Man kann aber auch Kartoffel- oder Semmelknödel dazu reichen. Etwas aufwendig, aber die Mühe lohnt sich... es ist einfach mega-ober-lecker.Anmerkung: Für viele sind Eier in Verbindung mit Sauerkraut ein No-Go, man kann sie also auch weglassen.</Instructions>
      <Ingredients>['600 g Hackfleisch, halb und halb', '800 g Sauerkraut', '200 g Wurst, geräucherte (Csabai Kolbász)', '150 g Speck, durchwachsener, geräucherter', '100 g Reis', '1 m.-große Zwiebel(n)', '1 Zehe/n Knoblauch', '2 Becher Schmand', '1/2TL Kümmel, ganzer', '2 Lorbeerblätter', 'Salz und Pfeffer', '4 Ei(er) (bei Bedarf)', 'Paprikapulver', 'etwas Wasser', 'Öl']</Ingredients>
      <Day>1</Day>
      <Name>Gebratener Hasenrücken</Name>
      <Year>2009</Year>
      <Month>January</Month>
      <Weekday>Thursday</Weekday>
    </row>
    <row>
      <index>1</index>
      <Url>https://www.chefkoch.de/rezepte/2718181424631245/</Url>
      <Instructions>Vorab folgende Bemerkung: Alle Mengen sind Circa-Angaben und können nach Geschmack variiert werden!Das Gemüse putzen und in Stücke schneiden (die Tomaten brauchen nicht geschält zu werden!). Alle Zutaten werden im Mixer püriert, das muss wegen der Mengen in mehreren Partien geschehen, und zu jeder Partie muss auch etwas von der Brühe gegeben werden. Auch das Toastbrot wird mitpüriert, es dient der Bindung. Am Schluss lässt man das Öl bei laufendem Mixer einfließen. In einer großen Schüssel alles gut verrühren und für mindestens eine Stunde im Kühlschrank gut durchkühlen lassen.Mit frischem Baguette an heißen Tagen ein Hochgenuss.Tipps: Wer mag, kann in kleine Würfel geschnittene Tomate, Gurke und Zwiebel separat dazu reichen.Die Suppe eignet sich hervorragend zum Einfrieren, so dass ich immer diese große Menge zubereite, um den Arbeitsaufwand gering zu halten.</Instructions>
      <Ingredients>['1 kg Strauchtomate(n)', '1 Gemüsezwiebel(n)', '1 Salatgurke(n)', '1 Paprikaschote(n) nach Wahl', '6 Zehe/n Knoblauch', '1 Chilischote(n)', '15 EL Balsamico oder Weinessig', '6 EL Olivenöl', '4 Scheibe/n Toastbrot', 'Salz und Pfeffer', '1 kl. Dose/n Tomate(n), geschälte, oder 1 Pck. pürierte Tomaten', '1/2Liter Brühe, kalte']</Ingredients>
      <Day>1</Day>
      <Name>Pilz Stroganoff</Name>
      <Year>2017</Year>
      <Month>July</Month>
      <Weekday>Saturday</Weekday>
    </row>'''
  st.code(code, language='xml')
  
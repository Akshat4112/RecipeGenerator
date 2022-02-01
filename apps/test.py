from big_letters import *

    
def build_headline(text):
    try:
        big = ''
        text = text.upper()
        
        for i in range(6):
            for char in text:
                rows = letters[char].split("\n")
                big = big + "\n".join(rows[i:i+1])
            big += "\n"
        return big       
    except AssertionError as e:
        print(e)

pupu = "ebbg"
print(build_headline(pupu))
import streamlit as st
def app():
    st.subheader("DTD for the Dataset")
    code  = ''' <?xml encoding="UTF-8"?>

    <!ELEMENT data (row)+>
    <!ATTLIST data
        xmlns CDATA #FIXED ''>

    <!ELEMENT row (index,Url,Instructions,Ingredients,Day,Name,Year,Month,Weekday)>
    <!ATTLIST row
        xmlns CDATA #FIXED ''>

    <!ELEMENT index (#PCDATA)>
    <!ATTLIST index
        xmlns CDATA #FIXED ''>

    <!ELEMENT Url (#PCDATA)>
    <!ATTLIST Url
        xmlns CDATA #FIXED ''>

    <!ELEMENT Instructions (#PCDATA)>
    <!ATTLIST Instructions
        xmlns CDATA #FIXED ''>

    <!ELEMENT Ingredients (#PCDATA)>
    <!ATTLIST Ingredients
        xmlns CDATA #FIXED ''>

    <!ELEMENT Day (#PCDATA)>
    <!ATTLIST Day
        xmlns CDATA #FIXED ''>

    <!ELEMENT Name (#PCDATA)>
    <!ATTLIST Name
        xmlns CDATA #FIXED ''>

    <!ELEMENT Year (#PCDATA)>
    <!ATTLIST Year
        xmlns CDATA #FIXED ''>

    <!ELEMENT Month (#PCDATA)>
    <!ATTLIST Month
        xmlns CDATA #FIXED ''>

    <!ELEMENT Weekday (#PCDATA)>
    <!ATTLIST Weekday
        xmlns CDATA #FIXED ''>
    '''
    st.code(code, language='xml')
    
import streamlit as st
def app():
    st.subheader("RelaxNG for the Dataset")
    code  = ''' 
    <?xml version="1.0" encoding="UTF-8"?>
    <grammar ns="" xmlns="http://relaxng.org/ns/structure/1.0">
        <define name="data">
            <element name="data">
                <ref name="attlist.data"/>
                <oneOrMore>
                    <ref name="row"/>
                </oneOrMore>
            </element>
        </define>
        <define name="attlist.data" combine="interleave">
            <empty/>
        </define>
        <define name="row">
            <element name="row">
                <ref name="attlist.row"/>
                <ref name="index"/>
                <ref name="Url"/>
                <ref name="Instructions"/>
                <ref name="Ingredients"/>
                <ref name="Day"/>
                <ref name="Name"/>
                <ref name="Year"/>
                <ref name="Month"/>
                <ref name="Weekday"/>
            </element>
        </define>
        <define name="attlist.row" combine="interleave">
            <empty/>
        </define>
        <define name="index">
            <element name="index">
                <ref name="attlist.index"/>
                <text/>
            </element>
        </define>
        <define name="attlist.index" combine="interleave">
            <empty/>
        </define>
        <define name="Url">
            <element name="Url">
                <ref name="attlist.Url"/>
                <text/>
            </element>
        </define>
        <define name="attlist.Url" combine="interleave">
            <empty/>
        </define>
        <define name="Instructions">
            <element name="Instructions">
                <ref name="attlist.Instructions"/>
                <text/>
            </element>
        </define>
        <define name="attlist.Instructions" combine="interleave">
            <empty/>
        </define>
        <define name="Ingredients">
            <element name="Ingredients">
                <ref name="attlist.Ingredients"/>
                <text/>
            </element>
        </define>
        <define name="attlist.Ingredients" combine="interleave">
            <empty/>
        </define>
        <define name="Day">
            <element name="Day">
                <ref name="attlist.Day"/>
                <text/>
            </element>
        </define>
        <define name="attlist.Day" combine="interleave">
            <empty/>
        </define>
        <define name="Name">
            <element name="Name">
                <ref name="attlist.Name"/>
                <text/>
            </element>
        </define>
        <define name="attlist.Name" combine="interleave">
            <empty/>
        </define>
        <define name="Year">
            <element name="Year">
                <ref name="attlist.Year"/>
                <text/>
            </element>
        </define>
        <define name="attlist.Year" combine="interleave">
            <empty/>
        </define>
        <define name="Month">
            <element name="Month">
                <ref name="attlist.Month"/>
                <text/>
            </element>
        </define>
        <define name="attlist.Month" combine="interleave">
            <empty/>
        </define>
        <define name="Weekday">
            <element name="Weekday">
                <ref name="attlist.Weekday"/>
                <text/>
            </element>
        </define>
        <define name="attlist.Weekday" combine="interleave">
            <empty/>
        </define>
        <start>
            <choice>
                <ref name="data"/>
            </choice>
        </start>
    </grammar>

    '''
    st.code(code, language='xml')
    
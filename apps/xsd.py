import streamlit as st
def app():
  st.subheader("XSD for the Dataset")
  code  = '''
  <?xml version="1.0" encoding="UTF-8"?>
  <xs:schema attributeFormDefault="unqualified" elementFormDefault="qualified" xmlns:xs="http://www.w3.org/2001/XMLSchema">
    <xs:element name="data" type="dataType"/>
    <xs:complexType name="rowType">
      <xs:sequence>
        <xs:element type="xs:string" name="index"/>
        <xs:element type="xs:string" name="Url"/>
        <xs:element type="xs:string" name="Instructions"/>
        <xs:element type="xs:string" name="Ingredients"/>
        <xs:element type="xs:string" name="Day"/>
        <xs:element type="xs:string" name="Name"/>
        <xs:element type="xs:string" name="Year"/>
        <xs:element type="xs:string" name="Month"/>
        <xs:element name="Weekday">
          <xs:simpleType>
            <xs:restriction base="xs:string">
              <xs:enumeration value="Thursday"/>
              <xs:enumeration value="Saturday"/>
              <xs:enumeration value="Monday"/>
              <xs:enumeration value="Tuesday"/>
              <xs:enumeration value="Sunday"/>
              <xs:enumeration value="Wednesday"/>
              <xs:enumeration value="Friday"/>
            </xs:restriction>
          </xs:simpleType>
        </xs:element>
      </xs:sequence>
    </xs:complexType>
    <xs:complexType name="dataType">
      <xs:sequence>
        <xs:element type="rowType" name="row" maxOccurs="unbounded" minOccurs="0"/>
      </xs:sequence>
    </xs:complexType>
  </xs:schema>
  '''
  st.code(code, language='xml')
  
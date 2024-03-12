import streamlit as st
import pandas as pd

if 'key' not in st.session_state:
    st.session_state['key'] = 'value'

if 'key' not in st.session_state:
    st.session_state['key'] = 'value'
st.set_page_config(
    page_title='Spreadsheet automation'
)
df = pd.read_csv('Master_Template_Upload.csv')
st.write('Welcome')
st.markdown(
    """In the forthcoming page, enter the information into the relevant boxes
    **Once you're sure the data is correct, click the 'Submit' button at the bottom of the page**
    Select the data entry section from the tab to the left to begin adding the data"""
)



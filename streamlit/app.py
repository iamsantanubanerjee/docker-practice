import streamlit as st
import requests

st.title('String Reversal App')
st.write('Enter a string and get its reverse.')

input_string = st.text_input('Input string:')

if st.button('Reverse'):
    if input_string:
        response = requests.post('http://127.0.0.1:5001/reverse', json={'input': input_string})
        if response.status_code == 200:
            output = response.json().get('output')
            st.write('Reversed string:', output)
        else:
            st.write('Error:', response.text)
    else:
        st.write('Please enter a string.')

# Import Library
import streamlit as st

# Import halaman streamlit yang sudah dibuat
import eda
import prediction


# Tombol navigasi
navigasi = st.sidebar.selectbox('Choose page :', ('EDA', 'Model Prediction'))

if navigasi == 'Model Prediction':
    prediction.run()
else:
    eda.run()
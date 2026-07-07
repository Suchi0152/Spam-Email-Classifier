import streamlit as st
from src.predict import predict_email

st.title('AI Spam Email Classifier')

email = st.text_area('Enter Email')

if st.button('Predict'):
    result, confidence = predict_email(email)
    st.write('Prediction:', result)
    st.write('Confidence:', confidence)

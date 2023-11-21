import streamlit as st
import datetime

st.title("Formulaire de contact")

with st.form('Formulaire de contact'):
    name = st.text_input('Tapez votre nom')
    mail = st.text_input('Tapez votre mail')
    age = st.slider('Quel est votre age ?', 0, 130, 25)
    date = st.date_input("Date de naissance", datetime.date(2019, 7, 6))

    if st.form_submit_button('Envoyer'):
        st.write(name  + " , vous avez " + str(age) + " ans.")

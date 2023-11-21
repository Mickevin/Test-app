import streamlit as st

st.title("Formulaire de contact")

with st.form('Formulaire de contact'):
    name = st.text_input('Tapez votre nom')
    age = st.slider('Quel est votre age ?', 0, 130, 25)

    if st.form_submit_button('Send'):
        st.write(name  + ", vous avez " + age + " ans.")

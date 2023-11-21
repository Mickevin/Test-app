import streamlit as st
import pandas as pd

a = "Bonjour"
df = pd.read_csv('data.csv')

def page_1():
    ### Title et markdown : st.title et st.markdown
    st.title("Application Streamlit")

    st.subheader("Sous-titre")

    st.write("Je suis une zone de texte")

    st.markdown("""
                # Titre

                ## Sous-titre

                texte
                """)


    ### Checkbox st.checkbox
    if st.checkbox("Show Dataframe"):
        st.write(df.head(10))

    ### Selectbox st.selectbox
    select_user = st.selectbox('Sélect a number : ', range(5))
    st.write(f"Your choice : {select_user}")


    ### Forms st.form, st.form_submit_button et st.select_slider
    with st.form('Formulaire 1'):
        name = st.text_input('Tape your Name')

        if st.form_submit_button('Send'):
            st.write(name)


    ### Columns st.columns

   
    ### Graphique Histogramme avec matplotlib.pyplot, seaborn et st.pyplot


    ### Image avec st.image
    st.image('https://www.alleycat.org/wp-content/uploads/2019/03/FELV-cat.jpg', width=200)
    
    
def page_2():
    st.title("Page 2")
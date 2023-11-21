### Import
from functions import *

### Config
st.set_page_config(
    page_title='Srteamlit App',
    page_icon='😉',
    layout="wide"
)

dict_page = {
    'Page 1' : page_1,
    'Page 2' : page_2
}

#page = st.selectbox("Pages : ", dict_page.keys())
#dict_page[page]()


page_sb = st.sidebar.selectbox("Pages : ", dict_page.keys())
dict_page[page_sb]()


### Graphique Histogramme px.histogram et st.plotly_chart



### Graphique Pie chart px.pie et st.plotly_chart



### + De graphiques ici : https://plotly.com/python/

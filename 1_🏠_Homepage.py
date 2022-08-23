import streamlit as st  
from PIL import Image


st.set_page_config(page_title="Siddhant_Jha",page_icon='👩‍💻')

st.title('Hi i am Siddhant')
image = Image.open('me image.jpeg')
col1, col2, col3 = st.columns([0.2, 5, 0.2])
col2.image(image, use_column_width=True)

st.subheader(" Hi welcome, are you new to this place my name is Siddhant i am an aspiring data scientist working on various projects across the fields of Machine Learning and also Deep learning , i also like to participate amon various ML competetions ,both online and offline in the recent past.") 
st.subheader(" Other than that this website of mine conatins all of my work which you can check on the Projects page and also feel free to Contact me personally or on public platfroms from the Contact page")


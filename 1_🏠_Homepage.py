import streamlit as st
import requests
from streamlit_lottie import st_lottie
st.set_page_config(page_title="Siddhant_Jha",page_icon='👩‍💻',layout='wide')

# About me
with st.container():
    st.title('Hi i am Siddhant :wave:')

    st.subheader(" Hi welcome, are you new to this place my name is Siddhant i am an aspiring data scientist working on various projects across the fields of Machine Learning and also Deep learning , i also like to participate in various ML competitions ,both online and offline in the recent past.") 
    st.subheader(" Other than that this website of mine conatins all of my work which you can check on the Projects page and also feel free to Contact me personally or on public platfroms from the Contact page")

# Load assets
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("Style/style.css")


lotte =load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_jaejabqz.json")
# What do i do ?

with st.container():
       st.write("---")
       left_column, right_column = st.columns(2)
       with left_column:
            st.header("What I do")
            st.write("##")
            st.write(
            """
            On my Substack I write about research in Machine Learning and Deep Learning :
            - I am currently in my Undergrad pursuing B.S in Data science at James Cook University , Australia.
            - I also make deployable Machine Learning projects available at my [Github Page ](https://github.com/SiddhantJha317).
            - I try to automate repetitive processes that I have to execute daily leveraging the power of Python.
            - I try to learn more and more Data science as time passes by me through various resources and try to educate people through my newsletter.
            - I am also passionate about the prospects of pure mathematical tools such Category Theory and Graphs, in improving neural network performance.
            If this sounds interesting to you, consider subscribing to my weekly Newsletter.
            """
            )
       with right_column:    
            st_lottie(lotte, height=500, key="coding")

with st.container():
    st.write('---')            
    st.header('My Projects')

with st.container():
    st.write('---')
    st.header('Education')




# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/e113681c572859dec58b20ac2d94b4db" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()    
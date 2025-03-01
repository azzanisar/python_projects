import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config (
    page_title="Contact",
    page_icon="📱",
)
st.title("Contact")

def load_contact(link):
     r=requests.get(link)
     if r.status_code != 200:
         return None
     return r.json()

lottie_contact= load_contact("https://assets2.lottiefiles.com/packages/lf20_hpyw99nb.json")
st_lottie(lottie_contact, height=275, key="news")

st.header(":mailbox: Get In Touch With Us!")

contact_form = """
<form action="https://formsubmit.co/YOUREMAIL@EMAIL.COM" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

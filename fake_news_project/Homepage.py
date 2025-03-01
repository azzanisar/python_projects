import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config (
    page_title="Homepage",
    page_icon="📱",
)

st.title("Main Page")
st.sidebar.success("Select a page above")

def load_homepage(animation):
     r=requests.get(animation)
     if r.status_code != 200:
         return None
     return r.json()

lottie_homepage= load_homepage("https://assets7.lottiefiles.com/packages/lf20_qmfs6c3i.json")

with st.container():
    st.write('---')
    left_column, right_column=st.columns(2)
    with left_column:
        st.header("Survey Questions for our Users")
    with right_column:
        st_lottie(lottie_homepage, height=300, key="news")

news_survey= st.radio("What sources do you use to look for news?", ("Twitter/Facebook/Instagram","Reading News on Google","TV"))
button1=st.button("Submit Answer")
if button1:
    st.write(news_survey)
    if news_survey == "Twitter/Facebook/Instagram":
        st.write("Fake news spreads 10 times faster on social media platforms than legitimate trusted news so make sure you are following reliable accounts")
    elif news_survey == "Reading News on Google":
        st.write("Google News collects some false stories among other accurate news it presents so therefore most of the time false information is more likely to spread faster to users")
    elif news_survey == "TV":
        st.write("%d %%  of news consumers say news from traditional sources can’t be trusted." % 44)

st.header("Choose your estimated ratio")
slider1=st.slider("What do you think is the ratio for fake news vs trusted news?", 1, 100)
if st.button("Submit Ratio"):
    if slider1 > 60:
      st.write("You got it right!")
    elif slider1 < 50:
        st.write("Generally about %d %% of news is fake on the internet" % 62)

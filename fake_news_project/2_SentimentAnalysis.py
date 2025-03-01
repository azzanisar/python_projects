import streamlit as st
import requests
from streamlit_lottie import st_lottie
from newspaper import Article
from textblob import TextBlob
import matplotlib.pyplot as plt

st.set_page_config (
    page_title="Sentiment Analysis",
    page_icon="📱",
)

st.title("Sentiment Analysis")

def load_sentiment(view):
    r=requests.get(view)
    if r.status_code != 200:
        return None
    return r.json()

lottie_sentiment= load_sentiment("https://assets10.lottiefiles.com/packages/lf20_x5Tg8Cv6dM.json")
with st.container():
    st.write('---')
    left_column, right_column=st.columns(2)
    with left_column:
        st.header("What are the sentiments behind the news?")
    with right_column:
        st_lottie(lottie_sentiment, height=300, key="sentiment")

def analyze_sentiment(text):
    """
    Performs sentiment analysis for the given text
    """
    # Perform sentiment analysis on the text.
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    # Determine the news status based on polarity.
    # Print the analysis results.
    if polarity > 0 and subjectivity < 0.5:
        result = st.write("Positive and objective")
    elif polarity > 0 and subjectivity > 0.5:
        result = st.write("Positive and subjective")
    elif polarity > 0 and subjectivity == 0.5:
        result = st.write("Positive and neutral content")
    elif polarity < 0 and subjectivity < 0.5:
        result = st.write("Negative and objective")
    elif polarity < 0 and subjectivity > 0.5:
        result = st.write("Negative and subjective")
    elif polarity < 0 and subjectivity == 0.5:
        result = st.write("Negative and neutral content")
    elif polarity == 0 and subjectivity < 0.5:
        result = st.write("Neutral and objective")
    elif polarity == 0 and subjectivity > 0.5:
        result = st.write("Neutral and subjective")
    elif polarity == 0 and subjectivity == 0.5:
        result = st.write("Neutral")
    else:
        result = st.write("Not able to calculate sentiment of this content! Try another input")

    st.write("Polarity: ", polarity)
    st.write("Subjectivity: ", subjectivity)
    st.write("News status: ", result)
    # Return the analysis results.
    return polarity, subjectivity, result


def get_article_sentiment():
    """
    Performs sentiment analysis for the given news link
    """
    # Get a news link input from the user
    url = st.text_input("Please enter a news link:", key="article_link")

    # Perform sentiment analysis on the news article
    if st.button("Analyze", key="article_analyze"):
        if url:
            article = Article(url)
            article.download()
            article.parse()
            text = article.text

            polarity, subjectivity, result = analyze_sentiment(text)
            if polarity > 0 and subjectivity < 0.5:
                result = st.write("Positive and objective")
            elif polarity > 0 and subjectivity > 0.5:
                result = st.write("Positive and subjective")
            elif polarity > 0 and subjectivity == 0.5:
                result = st.write("Positive and neutral content")
            elif polarity < 0 and subjectivity < 0.5:
                result = st.write("Negative and objective")
            elif polarity < 0 and subjectivity > 0.5:
                result = st.write("Negative and subjective")
            elif polarity < 0 and subjectivity == 0.5:
                result = st.write("Negative and neutral content")
            elif polarity == 0 and subjectivity < 0.5:
                result = st.write("Neutral and objective")
            elif polarity == 0 and subjectivity > 0.5:
                result = st.write("Neutral and subjective")
            elif polarity == 0 and subjectivity == 0.5:
                result = st.write("Neutral")
            else:
                result = st.write("Not able to calculate sentiment of this content! Try another input")

            # Display the analysis results.
            st.write("News content:")
            st.write(text)
            st.write("Polarity:", polarity)
            st.write("Subjectivity:", subjectivity)
            st.write("News status:", result)

            return polarity, subjectivity


def get_text_sentiment():
    """
    Performs sentiment analysis for the given text.
    """
    text = st.text_area("Please enter a news content:", key="news_content")

    if st.button("Analyze", key="text_analyze"):
        if text:
            polarity, subjectivity, result = analyze_sentiment(text)
            return polarity, subjectivity



polarities = []
subjectivities = []
choice = st.selectbox("Choose an option", ("Enter a text", "Enter a link" ))

if choice == "Enter a text":
    sentiment_result = get_text_sentiment()
    if sentiment_result is not None:
        polarity, subjectivity = sentiment_result
        polarities.append(polarity)
        subjectivities.append(subjectivity)
        st.write("Sentiment: polarity =", polarity, "subjectivity =", subjectivity)

elif choice == "Enter a link":
    sentiment_result = get_article_sentiment()
    if sentiment_result is not None:
        polarity, subjectivity = sentiment_result
        polarities.append(polarity)
        subjectivities.append(subjectivity)
        st.write("Sentiment: polarity =", polarity, "subjectivity =", subjectivity)

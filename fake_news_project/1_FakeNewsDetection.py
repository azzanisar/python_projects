from streamlit_lottie import st_lottie
import streamlit as st
import pandas as pd
import os
import numpy as np
import re
import nltk
from scipy.sparse import csr_matrix
import seaborn as sns
from nltk.corpus import stopwords
from random import randint
import requests
from bs4 import BeautifulSoup
from newspaper import Article
from xgboost import XGBClassifier
import torch
import openai
from transformers import BartTokenizer, BartForConditionalGeneration, pipeline
from matplotlib import pyplot as plt
from collections import Counter
from joblib import dump
from nltk.tokenize import word_tokenize
import pickle


st.set_page_config (
    page_title="Fake News Detection",
    page_icon="📱",
)


def load_fakenews(world):
     r=requests.get(world)
     if r.status_code != 200:
         return None
     return r.json()


lottie_fake= load_fakenews("https://assets7.lottiefiles.com/packages/lf20_aqbbxmsx.json")

with st.container():
    st.write('---')
    left_column, right_column=st.columns(2)
    with left_column:
        st.title("Fake News Detection")
    with right_column:
        st_lottie(lottie_fake, height=300, key="news")

# Define a function to extract and clean text from a URL
def extract_text_clean(url):

    # Make a request to the URL
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the text from the HTML content
    text = soup.get_text()

    # Remove non-alphabetic characters
    text = re.sub('[^a-zA-Z]', ' ', text)

    # Convert to lowercase
    text = text.lower()

    # Tokenize the text
    tokens = nltk.word_tokenize(text)

    # Remove stopwords
    stopwords = nltk.corpus.stopwords.words('english')
    tokens = [token for token in tokens if token not in stopwords]

    # Remove specific words
    remove_words = ['newsbbc', 'homepageskip', 'contentaccessibility', 'helpyour', 'accounthomenewssportreelworklifetravelfuturemore', 'menumore', 'menusearch', 'bbchomenewssportreelworklifetravelfutureculturemusictvweathersoundsclose', 'menubbc', 'newsmenuhomewar', 'ukraineclimatevideoworldukbusinesstechsciencestoriesmoreentertainment', 'artshealthworld', 'news', 'tvin', 'picturesreality', 'checknewsbeatlong', 'readsworldafricaasiaaustraliaeuropelatin', 'americamiddle', 'eastus']
    tokens = [token for token in tokens if token not in remove_words]

    # Join the tokens back into text
    text = ' '.join(tokens)

    return text


# Define a function to extract and clean text from a URL
def clean_text(text):

    # Remove non-alphabetic characters
    text = re.sub('[^a-zA-Z]', ' ', text)

    # Tokenize the text
    tokens = nltk.word_tokenize(text)

    # Remove stopwords
    stopwords = nltk.corpus.stopwords.words('english')
    tokens = [token for token in tokens if token not in stopwords]

    # Stem the tokens
    stemmer = nltk.stem.porter.PorterStemmer()
    tokens = [stemmer.stem(token) for token in tokens]

    # Join the tokens back into text
    text = ' '.join(tokens)

    return text

with open('ensemble_pickle', 'rb') as f:
    loaded_model=pickle.load(f)

with open('vec2_pickle', 'rb') as f:
    vec=pickle.load(f)

# Load the BART model and tokenizer for summarization
model_summarization = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
tokenizer_summarization = BartTokenizer.from_pretrained('facebook/bart-large-cnn')

def summarize_article(article_text):
    # Tokenize the article
    input_ids = tokenizer_summarization(article_text, max_length=1024, truncation=True, return_tensors='pt').input_ids

    # Generate a summary of the article
    summary_ids = model_summarization.generate(input_ids, num_beams=4, max_length=500, early_stopping=True)

    # Decode the summary text
    summary_text = tokenizer_summarization.decode(summary_ids.squeeze(), skip_special_tokens=True)

    return summary_text

def predict_article_ensemble(url):

    #get the article and summarize it using bert
    cleaned_text = extract_text_clean(url)
    summ_article = summarize_article(cleaned_text)

    # Set OpenAI API key
    openai.api_key = "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"

    #get gpt vote
    cont = f'{summ_article} do fact checking and provide 1 source at the end'
    completion = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=[{'role':'user', 'content':cont}])
    gpt_answer = completion.choices[0].message.content

    # Vectorize the text
    vectorized_text = vec.transform([cleaned_text])

    # Predict the class label prediction probability of the input text using the loaded model
    class_label = loaded_model.predict_proba(vectorized_text)[0][0]

    st.write(f"Estimated Fake news probability: {class_label*100:.2f}% \n {gpt_answer}")


#main app
def main():
    st.header("Enter a news article URL and the model will predict whether it is true or false news.")

    # Get user input
    url = st.text_input("Enter the news article URL:")

    if st.button("Predict"):
        if url:
            # Predict the class label and get GPT-3 response
            prediction = predict_article_ensemble(url)
            st.write(prediction)

if __name__ == "__main__":
    main()

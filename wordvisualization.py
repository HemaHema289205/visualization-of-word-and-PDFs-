import streamlit as st
import matplotlib.pyplot as plt
import pdfplumber
from docx import Document
import io
from wordcloud import WordCloud
from collections import Counter
import pandas as pd

def extract_text_from_pdf(iobytes):
    doc = pdfplumber.open(io.BytesIO(iobytes))
    pages = [page.extract_text() for page in doc.pages if page.extract_text()]
    return ' '.join(pages)

def extract_text_from_word(iobytes):
    doc = Document(io.BytesIO(iobytes))
    paras = [para.text for para in doc.paragraphs if para.text.strip()]
    return ' '.join(paras)

def show_wordcloud(text):
    image = WordCloud(width=800, height=400, background_color='white').generate(text)
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.imshow(image)
    ax.axis('off')
    st.pyplot(fig)

def show_frequency_chart(text, top_n=20):
    word_counts = Counter(text.lower().split())
    common_words = dict(word_counts.most_common(top_n))
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(common_words.keys(), common_words.values(), color='skyblue')
    ax.set_title(f"Top {top_n} Word Frequencies")
    ax.set_ylabel("Count")
    ax.set_xticks(range(len(common_words)))
    ax.set_xticklabels(common_words.keys(), rotation=45, ha='right')
    st.pyplot(fig)
def show_bigram_chart(text, top_n=20):
    words = text.lower().split()
    bigrams = [' '.join([words[i], words[i+1]]) for i in range(len(words)-1)]
    bigram_counts = Counter(bigrams)
    common_bigrams = dict(bigram_counts.most_common(top_n))
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(common_bigrams.keys(), common_bigrams.values(), color='salmon')
    ax.set_title(f"Top {top_n} Bigram Frequencies")
    ax.set_ylabel("Count")
    ax.set_xticks(range(len(common_bigrams)))
    ax.set_xticklabels(common_bigrams.keys(), rotation=45, ha='right')
    st.pyplot(fig)

def show_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    st.markdown("🧠 Sentiment Analysis")
    st.write(f"**Polarity:** {polarity:.2f} (−1 = negative, +1 = positive)")
    st.write(f"**Subjectivity:** {subjectivity:.2f} (0 = objective, 1 = subjective)")

    if polarity > 0.2:
        st.success("Overall sentiment is positive.")
    elif polarity < -0.2:
        st.error("Overall sentiment is negative.")
    else:
        st.info("Overall sentiment is neutral or mixed.")

def gen_visuals(uploaded):
    iobytes = uploaded.read()
    if uploaded.name.lower().endswith('pdf'):
        text = extract_text_from_pdf(iobytes)
    else:
        text = extract_text_from_word(iobytes)

    st.subheader("Choose Visualization Type")
    vis_type = st.radio("", ["Word Cloud", "Frequency Bar Chart","Bigram Bar Chart", "Sentiment Analysis"])

    if vis_type == "Word Cloud":
        show_wordcloud(text)
    elif vis_type == "Frequency Bar Chart":
        show_frequency_chart(text)
    elif vis_type == "Bigram Bar Chart":
        show_bigram_chart(text)
    elif vis_type == "Sentiment Analysis":
        show_sentiment(text)

# Streamlit UI
st.set_page_config(layout='centered')
st.title('📄 Word Visualizer: PDF & Word Files')
uploaded = st.file_uploader('Upload a PDF or Word file', type=['pdf', 'docx'])

if uploaded:
    gen_visuals(uploaded)

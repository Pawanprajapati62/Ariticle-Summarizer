import streamlit as st
import requests
import textwrap
import os
from dotenv import load_dotenv

load_dotenv()


API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
API_TOKEN = os.getenv("hugging_face_API_KEY")

headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

def summarize_chunk(chunk):
    payload = {
        "inputs": chunk,
        "parameters": {"min_length": 30, "max_length": 100},
        "options": {"wait_for_model": True}
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    result = response.json()
    return result[0]['summary_text'] if isinstance(result, list) else None

def split_text(text, max_words=400):
    wrapper = textwrap.TextWrapper(width=1000)
    words = text.split()
    return [" ".join(words[i:i+max_words]) for i in range(0, len(words), max_words)]

st.title("📄 Article Summarizer")
st.write("Paste an article below.")

article = st.text_area("Enter your article:", height=200)

if st.button("Summarize"):
    if not article.strip():
        st.warning("Please enter some text.")
    else:
        with st.spinner("Summarizing..."):
            chunks = split_text(article)
            full_summary = ""
            for idx, chunk in enumerate(chunks):
                st.write(f"⏳ Summarizing chunk {idx+1}/{len(chunks)}...")
                summary = summarize_chunk(chunk)
                if summary:
                    full_summary += summary + " "
                else:
                    st.error("Error in summarizing a chunk.")
            st.subheader("✅ Final Summary:")
            st.success(full_summary.strip())

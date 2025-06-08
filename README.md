# 🧠 Article Summarizer App

This is a **simple yet powerful web app** that summarizes long articles using Natural Language Processing (NLP) techniques.  
It uses the **Hugging Face API** and the `facebook/bart-large-cnn` model to generate short, clear summaries from large chunks of text.

Built using **Streamlit**, it's super easy to use — just paste your text and get a smart summary in seconds.

---

## 🔧 What This App Can Do

✅ Summarize **very long articles** (even multiple pages)  
✅ Automatically splits big articles into chunks  
✅ Uses **pretrained transformer models** from Hugging Face  
✅ No need to download or train anything locally  
✅ Clean and beginner-friendly web interface with Streamlit  

---

## 🚀 How to Run the App

### 1. Clone the project

```bash
git clone https://github.com/your-username/article-summarizer
cd article-summarizer

### 2. Install the required libraries
```bash
pip install streamlit requests

### 3. Add your Hugging Face API token
Get your token from: https://huggingface.co/settings/tokens

Open the script and replace this line:
```bash
API_TOKEN = "your_huggingface_api_key_here"
with:
```bash
API_TOKEN = "your_real_api_key"

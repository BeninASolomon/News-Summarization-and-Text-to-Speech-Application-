# News-Summarization-and-Text-to-Speech-Application
This application extracts news articles related to a given company, performs sentiment analysis, compares sentiment trends across articles, and generates a Hindi text-to-speech (TTS) output. Users can input a company name and receive a structured sentiment report along with an audio summary.


* Scrapes top 10 news articles (MoneyControl)
* Performs Sentiment Analysis (Positive, Negative, Neutral)
* Compares Sentiment Trends across articles
* Generates Hindi Audio Output (Google TTS)
* Simple Web UI (Streamlit)
* Backend APIs (FastAPI)

app.py: Streamlit UI for user interaction
api.py: FastAPI backend for news & sentiment APIs
utils.py: Helper functions (scraping, sentiment, TTS)
README.txt: Project documentation

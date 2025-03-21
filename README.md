# News-Summarization-and-Text-to-Speech-Application
This application extracts news articles related to a given company, performs sentiment analysis, compares sentiment trends across articles, and generates a Hindi text-to-speech (TTS) output. Users can input a company name and receive a structured sentiment report along with an audio summary.





News Summarization and Text-to-Speech Application

Overview

This project is a News Summarization and Text-to-Speech (TTS) Application that extracts news articles, summarizes them using NLP techniques, and converts the summarized text into speech. The application is built using Python and leverages NLP libraries for text processing and TTS conversion.

Features

Extracts news articles from URLs or text input

Uses NLP techniques for automatic text summarization

Converts summarized text into speech using TTS

Provides a user-friendly interface for interaction

Dependencies

Ensure you have the following dependencies installed before running the application:

pip install -r requirements.txt

Required Libraries:

requests - To fetch news articles from web sources

beautifulsoup4 - For web scraping (if applicable)

nltk - For natural language processing and summarization

gTTS - Google Text-to-Speech for audio conversion

flask (if web-based) - To create a simple web interface

Installation & Setup

Clone the Repository:

git clone https://github.com/BeninASolomon/News-Summarization-and-Text-to-Speech-Application.git
cd News-Summarization-and-Text-to-Speech-Application

Install Dependencies:

pip install -r requirements.txt

Run the Application:

python app.py

Folder
* app.py: Streamlit UI for user interaction (Main file)
* api.py: FastAPI backend for news & sentiment APIs
* utils.py: Helper functions (scraping, sentiment, Text To Speech)
* README.md: Project documentation
* requirements.txt: Necessary libraries

Usage

Input a news article URL or paste raw text

Click on Summarize to generate a shorter version of the news

Click on Convert to Speech to hear the summarized text

Download the audio file for offline listening (if implemented)


Contributors

Benin A. Solomon (@BeninASolomon)

License

This project is licensed under the MIT License.

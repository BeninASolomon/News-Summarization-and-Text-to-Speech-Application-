# News Summarization and Text-to-Speech Application

## Overview

This project is a News Summarization and Text-to-Speech (TTS) Application that extracts news articles, summarizes them using NLP techniques, and converts the summarized text into speech. The application is built using Python and leverages NLP libraries for text processing and TTS conversion.

## Features

* Extracts news articles from URLs or text input
* Converts summarized text into speech using TTS
* Provides a user-friendly interface for interaction
* APIs enable interaction between frontend and backend
* Deployed on Hugging Face Spaces for public access

## Dependencies

Ensure you have the following dependencies installed before running the application:

* pip install -r requirements.txt

Required Libraries:

* requests - To fetch news articles from web sources
* beautifulsoup4 - For web scraping (if applicable)
* nltk - For natural language processing and summarization
* gTTS - Google Text-to-Speech for audio conversion


## Installation & Setup

Clone the Repository:
* git clone https://github.com/BeninASolomon/News-Summarization-and-Text-to-Speech-Application-.git
* cd News-Summarization-and-Text-to-Speech-Application-

Install Dependencies:
* pip install -r requirements.txt

Run the Application:
* streamlit run app.py

## API Development

The application exposes APIs for:
* News Extraction API - Fetches and summarizes news articles.
* Sentiment Analysis API - Analyzes and categorizes sentiment.
* TTS API - Converts summarized text into Hindi speech.

## Deployment on Hugging Face Spaces

The application is deployed on Hugging Face Spaces for public use. You can access it here:
* [News Summarization and TTS App](https://huggingface.co/spaces/BeninASolomon/NewsSummarizationTTS)

To deploy manually:
* Create a Hugging Face Space
* Select Python - Streamlit
* Push code to the Hugging Face repository

Folder
* app.py: Streamlit UI for user interaction (Main file)
* api.py: FastAPI backend for news & sentiment APIs
* utils.py: Helper functions (scraping, sentiment, Text To Speech)
* README.md: Project documentation
* requirements.txt: Necessary libraries

Usage

* Input a news article URL 
* Click on Summarize to generate a shorter version of the news
* Click on Convert to Speech to hear the summarized text


Contributors

Benin Solomon A (@BeninASolomon)


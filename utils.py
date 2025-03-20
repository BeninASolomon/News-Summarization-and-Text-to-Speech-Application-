import requests
from bs4 import BeautifulSoup
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from gtts import gTTS
from deep_translator import GoogleTranslator
def fetch_news(company_name):
    url = f"https://www.moneycontrol.com/news/tags/{company_name}.html"
    headers = {"User-Agent": "Mozilla/5.0"}   
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return {"error": "Failed to fetch news"}
    soup = BeautifulSoup(response.text, "html.parser")
    articles = []
    for article in soup.find_all("li", class_="clearfix")[:10]:  # Get top 10 articles
        title = article.find("h2").text.strip()
        summary = article.find("p").text.strip() if article.find("p") else "No summary available."
        link = article.find("a")["href"]       
        articles.append({
            "title": title,
            "summary": summary,
            "url": link
        })
    return articles
def analyze_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(text)
    if score["compound"] >= 0.05:
        sentiment = "Positive"
    elif score["compound"] <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    return {"score": score["compound"], "sentiment": sentiment}


def translate_to_hindi(text):
    return GoogleTranslator(source='auto', target='hi').translate(text)

def generate_hindi_audio(text, output_file="output.mp3"):
    hindi_text = translate_to_hindi(text)  # First translate the text to Hindi
    tts = gTTS(hindi_text, lang="hi")  # Convert translated text to speech
    tts.save(output_file)
    return output_file

def compare_sentiments(news_articles):
    data = []
    for article in news_articles:
        sentiment = analyze_sentiment(article["summary"])
        data.append({
            "Title": article["title"],
            "Sentiment": sentiment["sentiment"],
            "Score": sentiment["score"]
        })
    df = pd.DataFrame(data)
    return df.groupby("Sentiment")["Score"].count().to_dict()

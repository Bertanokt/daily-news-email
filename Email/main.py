import requests
from send_email import send_email
from datetime import datetime
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os

load_dotenv()
today = datetime.now().strftime("%Y-%m-%d")

topic = ("Turkey")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
NEWS_API_KEY= os.getenv("NEWS_API_KEY")

url = ("https://newsapi.org/v2/everything?" 
      f"q={topic}&"
       f"from={today}"
      "to=2026-04-15&sortBy=popularity&"
      f"apiKey= {NEWS_API_KEY}"
      "language=en")

#Make request
response = requests.get(url)

# Get a dictionary with a data
content = response.json()
articles = content["articles"]

#AI summarizing the news
model = init_chat_model(model="gemini-3-flash-preview",
                        model_provider="google-genai",
                        api_key = GOOGLE_API_KEY)
prompt = f"""
You are a news summarizer.
Write a two short paragraph analyzing those news.
Here are the news articles: {articles} """

response = model.invoke(prompt)
response_str = response.content[0]["text"]
print(response_str)

body = "Subject: News Summary\n\n" + response_str + "\n\n"

body = body.encode("utf-8")
send_email(message=body)

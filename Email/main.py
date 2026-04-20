import requests
from send_email import send_email
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv()

today = datetime.now().strftime("%Y-%m-%d")
yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")

topic = "Turkey"
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

url = ("https://newsapi.org/v2/everything?" 
       f"q={topic}&"
       f"from={yesterday}&"
       f"to={today}&"
       "sortBy=popularity&"
       f"apiKey={NEWS_API_KEY}&"
       "language=en")

response = requests.get(url)
content = response.json()

if content.get("totalResults", 0) == 0:
    print("Haber bulunamadı")
    exit()

articles = content["articles"][:10]

body = "Subject: Today's Turkey News\n\n"
for article in articles:
    body += f"• {article['title']}\n"
    body += f"  {article['description'] or ''}\n"
    body += f"  {article['url']}\n\n"

body = body.encode("utf-8")
send_email(message=body

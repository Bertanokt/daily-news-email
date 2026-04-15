import requests
from send_email import send_email
from datetime import datetime

today = datetime.now().strftime("%Y-%m-%d")

topic = ("Turkey")
API_KEY= "635a70c8b1e1402daa3116a4aeecdd89"

url = ("https://newsapi.org/v2/everything?" 
      f"qintitle={topic}&"
       f"from={today}"
      "to=2026-04-15&sortBy=popularity&"
      "apiKey=635a70c8b1e1402daa3116a4aeecdd89&"
      "language=en")

#Make request
response = requests.get(url)

# Get a dictionary with a data
content = response.json()

#Access the article titles and description
body = "Subject: Today's news\n\n"
for article in content["articles"][:20]:
    if article["title"] is not None:
        body += article["title"] + "\n"
        body += (article["description"] or "") + "\n"
        body += article["url"] + "\n\n"


body = body.encode("utf-8")
send_email(message=body)

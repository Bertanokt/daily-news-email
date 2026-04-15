import requests
from send_email import send_email
topic = ("apple")
API_KEY= "635a70c8b1e1402daa3116a4aeecdd89"

url = ("https://newsapi.org/v2/everything?" 
      f"q={topic}&"
       "from=2026-04-12&"
      "to=2026-04-15&sortBy=popularity&"
      "apiKey=635a70c8b1e1402daa3116a4aeecdd89&"
      "language=en")

#Make request
request = requests.get(url)

# Get a dictionary with a data
content = request.json()

#Access the article titles and description
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
       body = "Subject: Today's news"+ "\n" + body + article["title"] + "\n" + article["description"] + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
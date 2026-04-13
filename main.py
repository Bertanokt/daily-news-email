import requests

API_KEY= "635a70c8b1e1402daa3116a4aeecdd89"
url = "https://newsapi.org/v2/everything?q=apple&from=2026-04-12&to=2026-04-12&sortBy=popularity&apiKey=635a70c8b1e1402daa3116a4aeecdd89"
#Make request
request = requests.get(url)
# Get a dictionary with a data
content = request.json()
#Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
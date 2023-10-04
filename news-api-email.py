import requests

api_key = "83eb3850927e41d9b49f340c8f21287b"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2023-09-04&sortBy=publishedAt&apiKey=" \
      "83eb3850927e41d9b49f340c8f21287b"

# Make a request
request = requests.get(url)

# Got a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])

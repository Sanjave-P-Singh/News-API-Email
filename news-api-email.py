import requests
from send_email import send_email

topic = "tesla"

api_key = "83eb3850927e41d9b49f340c8f21287b"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "sortBy=publishedAt&" \
      "apiKey=83eb3850927e41d9b49f340c8f21287b&" \
      "language=en"

# Make a request
request = requests.get(url)

# Got a dictionary with data
content = request.json()

# Access the article titles and description
body = "Subject: Today's news " + "\n"
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" \
               + article["description"] + "\n" \
               + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)

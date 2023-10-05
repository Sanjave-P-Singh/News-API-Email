import requests
from send_email import send_email

topic = "tesla"

api_key = "Will be found in the ReadMe"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "sortBy=publishedAt&" \
      "apikey= Will be found in the ReadMe&" \
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

import requests

COMPANY_NAME = "Tesla Inc"

def get_news(api_key):
    response = requests.get(url="https://newsapi.org/v2/everything", params={
        "q": COMPANY_NAME,
        "apiKey": api_key
    })
    response.raise_for_status()
    data = response.json()
    articles = data["articles"][:3]
    return articles

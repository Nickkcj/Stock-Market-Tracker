from twilio.rest import Client
from src.api.news_api import get_news
from config import ACCOUNT_SID, AUTH_TOKEN, TWILIO_PHONE, MY_PHONE, NEWS_API_KEY

def send_sms(percentage_change):
    percentage_change = round(percentage_change * 100, 2)
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    articles = get_news(NEWS_API_KEY)  
    news = ""
    for article in articles:
        news += f"Headline: {article['title']}\nBrief: {article['description']}\n\n"

    message = client.messages.create(
        from_=TWILIO_PHONE,
        to=MY_PHONE,
        body=f"TSLA: {'🔺' if percentage_change > 0 else '🔻'}{percentage_change}%\n{news}"
    )

    print(message.status)

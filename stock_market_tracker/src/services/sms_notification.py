from twilio.rest import Client
from src.api.news_api import get_news

ACCOUNT_SID = 'ACc480c80f3ae3bce92a7300967356fbd7'
AUTH_TOKEN = 'e58c037bad414f14d8445b7ff9c11850'
TWILIO_PHONE = '+13074413229'
MY_PHONE = '+5548998607422'

def send_sms(percentage_change):
    percentage_change = round(percentage_change * 100, 2)
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    articles = get_news('4c45b2450d984eacafcb418e68e99573')  
    news = ""
    for article in articles:
        news += f"Headline: {article['title']}\nBrief: {article['description']}\n\n"

    message = client.messages.create(
        from_=TWILIO_PHONE,
        to=MY_PHONE,
        body=f"TSLA: {'🔺' if percentage_change > 0 else '🔻'}{percentage_change}%\n{news}"
    )

    print(message.status)

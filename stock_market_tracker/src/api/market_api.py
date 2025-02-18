import requests
from src.services.sms_notification import send_sms

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

def get_stock_data(api_key):
    response = requests.get(url="https://www.alphavantage.co/query", params={
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": api_key
    })
    response.raise_for_status()
    data = response.json()
    data_list = list(data["Time Series (Daily)"].values())
    check_stock_price(data_list)

def check_stock_price(data):
    yesterday_data = data[0]
    day_before_yesterday_data = data[3]

    yesterday_closing_price = float(yesterday_data["4. close"])
    day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])

    percentage_change = (yesterday_closing_price - day_before_yesterday_closing_price) / day_before_yesterday_closing_price
    if abs(percentage_change) > 0.05:
        send_sms(percentage_change)

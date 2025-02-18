# 📈 Stock Alert and News SMS Service

This project monitors the stock price of **Tesla (TSLA)**, checks for significant changes, and sends an SMS alert along with the latest news! 🚀

---

## 📋 **Features**
- ✅ **Stock Price Monitoring**: Fetches daily stock prices using the [Alpha Vantage API](https://www.alphavantage.co/).
- 📉 **Price Change Detection**: Detects price changes of 5% or more.
- 📰 **News Fetching**: Retrieves the latest 3 news articles about Tesla from the [News API](https://newsapi.org/).
- 📲 **SMS Alerts**: Sends an SMS with the percentage change and news headlines using [Twilio](https://www.twilio.com/).

---

## 📁 **Project Structure**
```
/project-root
│
├── /src
│   ├── /api
│   │   ├── market_api.py      # API for fetching stock prices
│   │   └── news_api.py        # API for fetching news articles
│   │
│   ├── /services
│   │   └── sms_notification.py # Service for sending SMS notifications
│   │
│   └── main.py                # Entry point of the application
│
└── /config
    └── settings.py            # Configuration and API keys (optional)
```

---

## 🚀 **How It Works**
1. **Stock Monitoring**: `main.py` triggers the stock price check.
2. **Price Comparison**: If a price change of ±5% is detected, it fetches the latest news and prepares the SMS.
3. **News Fetch**: Retrieves the latest news articles about Tesla.
4. **SMS Alert**: Combines the percentage change and news headlines into an alert and sends it via Twilio.

---

## 🛠 **Setup and Usage**

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Nickkcj/Stock-Market-Tracker.git
   cd stock_market_tracker
   ```

2. **Install dependencies** (ensure Python is installed):
   ```bash
   pip install -r requirements.txt
   ```

3. **Update API keys**:
   - Add your API keys and Twilio credentials to the `settings.py` file or directly in the services.

4. **Run the project**:
   ```bash
   python src/main.py
   ```

---

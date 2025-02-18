from api.market_api import get_stock_data
from config import ALPHA_VANTAGE_API_KEY


def main():
    get_stock_data(ALPHA_VANTAGE_API_KEY)


if __name__ == "__main__":
    main()

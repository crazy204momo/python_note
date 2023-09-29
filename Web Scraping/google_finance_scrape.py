import requests as r
from bs4 import BeautifulSoup
from dataclasses import dataclass
from tabulate import tabulate

@dataclass
class Stock:
    ticker: str
    exchange: str
    price: float=0
    currency: str="USD"
    usd_price: float=0

    def __post_init__(self):
        price_info = get_price_information(self.ticker, self.exchange)
        if price_info["ticker"] ==self.ticker:
            self.price = price_info["price"]
            self.currency = price_info["currency"]
            self.usd_price = price_info["usd_price"]

@dataclass
class Position:
    stock: Stock
    quantity: int

@dataclass
class Portfolio:
    positions: list[Position]

    def get_total_value(self):
        total_value = 0

        for position in self.positions:
            total_value += position.quantity * position.stock.usd_price
        return total_value

#https://www.google.com/finance/quote/AAPL:NASDAQ
def get_price_information(ticker, exchange):
    url = f"https://www.google.com/finance/quote/{ticker}:{exchange}"
    resp = r.get(url)
    soup = BeautifulSoup(resp.content, 'lxml')
    price_div = soup.find("div", attrs={"data-last-price": True})
    price = float(price_div["data-last-price"])
    currency = price_div["data-currency-code"]
    usd_price = round(currency_to_USD(currency)*price,2)
    return {
        "ticker": ticker,
        "exchange": exchange,
        "price": price,
        "currency": currency,
        "usd_price": usd_price
    }
#https://www.google.com/finance/quote/CAD-USD
def currency_to_USD(currency):
    if currency!='USD':
        url = f"https://www.google.com/finance/quote/{currency}-USD"
        resp = r.get(url)
        soup = BeautifulSoup(resp.content, 'lxml')
        price_div = soup.find("div", attrs={"data-last-price": True})
        currency_value = float(price_div["data-last-price"])
        return currency_value
    else:
        return 1 

def display_portfolio_summary(portfolio):
    if not isinstance(portfolio, Portfolio):
        raise TypeError("Please provide instance of Portfolio type")
    
 


if __name__ == "__main__":
    print(get_price_information("AAPL", "NASDAQ"))
    print(get_price_information("SHOP", "NYSE"))
    print(Stock('SHOP','TSE'))
    print(Position(Stock('SHOP','TSE'),0))
    shop=Stock('SHOP','TSE')
    msft=Stock('MSFT','NASDAQ')
    googl=Stock('GOOGL','NASDAQ')
    portfolio=Portfolio([Position(shop,10),Position(msft,2),Position(googl,30)])
    print(portfolio.get_total_value())
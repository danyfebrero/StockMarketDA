import requests, json, subprocess
from os import path
from keys import keyAlphaVantage



stock_cache = "stockcache.json"


def main():
    stock = LoadStockData()
    print(f"Stock Symbol: {stock['Meta Data']['2. Symbol']}")
    print(f"Last Refreshed: {stock['Meta Data']['3. Last Refreshed']}")
    print(f"Months on Records: {len(stock['Monthly Time Series'])}")
    print("")
    
def GetStockSymbol():
    stock_symbol = input("Enter the desired stock symbol: ")
    return stock_symbol

def StockUrl():
    """Creates a url to donwload the stock data from the API"""

    stock = GetStockSymbol()
    time_series = {
        "daily": "TIME_SERIES_DAILY",
        "weekly": "TIME_SERIES_WEEKLY",
        "monthly": "TIME_SERIES_MONTHLY"
        }
    data_type = {
        "json": "json",
        "csv": "csv"
        }
    # replace the apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = f"https://www.alphavantage.co/query?function={time_series['monthly']}&symbol={stock.upper()}&apikey={keyAlphaVantage}&datatype={data_type['json']}"
    
    # remove this block after test
    stock_name = f"{stock.lower()}.{data_type['csv']}"
    stock_url = f"https://www.alphavantage.co/query?function={time_series['monthly']}&symbol={stock.upper()}&apikey={keyAlphaVantage}&datatype={data_type['csv']}"
    with requests.Session() as s:
        _stockdata = s.get(stock_url)
        with open(stock_name, "wb") as file:
            file.write(_stockdata.content)
    # end of block
    return url

def DownloadStockData():
    """Save the stock data to local disc"""

    with requests.Session() as s:
        stockdata = s.get(StockUrl())
        with open(stock_cache, "wb") as file:
            file.write(stockdata.content)

def LoadStockData():
    """Loads the data from the local files or API"""
    if path.exists(stock_cache):
        subprocess.call(["clear"])
        user_input = input("Do you want to work with the data from the last session? (yes / no): ")
        subprocess.call(["clear"])
        if user_input[0].lower() == "n":
            DownloadStockData()
    else:
        DownloadStockData()
    
    with open(stock_cache) as f:
        stock_data = json.load(f)
    return stock_data

if __name__ == "__main__":
    main()
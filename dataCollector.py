import requests, csv, subprocess
from os import path
from keys import get_key


keyAlphaVantage = get_key()
stock_cache_file = "stockcache.csv"
stock_cache = []

def main():
    stock = LoadStockData()
    print(len(stock))
    
def GetStockSymbol():
    symbols = input("Enter the desired stock symbols separated by a space between them: ")
    stock_symbols = symbols.split(" ")
    return stock_symbols

def StockUrl():
    """Creates urls to donwload the stock data from the API"""
    urls =[]
    symbol = GetStockSymbol()
    stock_data_functions =["OVERVIEW", "TIME_SERIES_MONTHLY"]   # "TIME_SERIES_DAILY", "TIME_SERIES_WEEKLY", 
    data_type = {
        "json": "json",
        "csv": "csv"
        }
    # replace the apikey below with your own key from https://www.alphavantage.co/support/#api-key
    for function in stock_data_functions:
        urls.append(f"https://www.alphavantage.co/query?function={function}&symbol={symbol.upper()}&apikey={keyAlphaVantage}&datatype={data_type['csv']}")
    return urls

def DownloadStockData():
    """Save the stock data to local disc"""
    with requests.Session() as s:
        stock_data = s.get(StockUrl())
        stock_name = f"{symbol.lower()}.{data_type['csv']}"

        with open(stock_name, "wb") as file:
            file.write(stock_data.content)

def LoadStockData():
    """Loads the data from the local files or API"""
    if path.exists(stock_cache_file) and path.getsize(stock_cache_file) != 0:
        with open(stock_cache_file,"r") as file:

        subprocess.call(["clear"])
        user_input = input("Do you want to work with the data from the last session? (yes / no): ")
        subprocess.call(["clear"])
        if user_input[0].lower() == "n":
            DownloadStockData()
    else:
        DownloadStockData()
    
    with open(stock_cache_file) as f:
        stock_data = csv.reader(f)
    return stock_data

if __name__ == "__main__":
    main()
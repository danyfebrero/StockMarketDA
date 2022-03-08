from operator import contains
from typing import Counter
import requests, csv, subprocess
from os import path
from os import remove
from keys import get_key

keyAlphaVantage = get_key()
cache_file_name = "stockscache.csv"
stock_data_functions =["OVERVIEW", "TIME_SERIES_MONTHLY"] # "TIME_SERIES_DAILY", "TIME_SERIES_WEEKLY",


def main():
   print(list_of_stocks())

def delete_cache(stock_list):
    for stock in stock_list:
        for data_funtion in stock_data_functions:
            file_name = f"{stock.lower()}_{data_funtion}.csv"
            if path.exists(file_name):
                remove(file_name)

def make_stock_urls(stock):
    """Creates urls to donwload the stock data from the API"""
    urls =[]
    data_type = {
        "json": "json",
        "csv": "csv"
        }
    # get your API key from https://www.alphavantage.co/support/#api-key
    for function in stock_data_functions:
        urls.append(f"https://www.alphavantage.co/query?function={function}&symbol={stock.upper()}&apikey={keyAlphaVantage}&datatype={data_type['csv']}")
    return urls

def load_cache():
    stocks_cache = []
    with open(cache_file_name,"r") as file:
        reader = csv.reader(file)
        stocks_cache = next(reader) 
    return(stocks_cache)        

def ask_stocks_symbols():
    symbols = input("Enter the desired stock symbols separated by a space between them: ")
    stocks_symbols = symbols.split(" ")
    return(stocks_symbols)

def save_cache(stock_symbols):
    with open(cache_file_name, "w") as file:
        writer = csv.writer(file)
        writer.writerow(stock_symbols)

def download_stocks_data(stock_list):
    for stock in stock_list:
        urls = make_stock_urls(stock)
        counter = 0
        for url in urls:
            with requests.Session() as s:
                stock_data = s.get(url)
                stock_name = f"{stock.lower()}_{stock_data_functions[counter]}.csv"
            with open(stock_name, "wb") as file:
                file.write(stock_data.content)
            counter += 1

def list_of_stocks():
    if path.exists(cache_file_name) and path.getsize(cache_file_name) != 0:
        stock_symbols = load_cache()
        while True:
            user_input = input("Do you want to work with the data from the last session? (yes / no): ").lower()
            if user_input[0] == "y" or user_input[0] == "n":
                break
        if user_input[0] == "n":
            delete_cache(stock_symbols)
            stock_symbols = ask_stocks_symbols()
            save_cache(stock_symbols)
            download_stocks_data(stock_symbols)
    else:             
        stock_symbols = ask_stocks_symbols()
        save_cache(stock_symbols)
        download_stocks_data(stock_symbols)
    return (stock_symbols)

if __name__ == "__main__":
    main()
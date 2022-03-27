import requests, csv, json, csv
from keys import load_key
import pandas as pd
import plotly.graph_objects as go

keyAlphaVantage = load_key()
stock_data_functions =["OVERVIEW", "TIME_SERIES_DAILY"] # "TIME_SERIES_MONTHLY", "TIME_SERIES_WEEKLY", "EARNINGS"

def main():
    data, over = get_stocks_data("AAPL")
    fig = create_candlestick_chart(data, over['Name'])
    fig.show()

    
def file_extension(data_function):
    if "OVERVIEW" in data_function or "EARNINGS" in data_function:
        file_ext = "json"
    else:
        file_ext = "csv"
    return(file_ext)

def make_stock_urls(stock):
    """Creates urls to donwload the stock data from the API"""
    urls =[]
    # get your API key from https://www.alphavantage.co/support/#api-key
    for function in stock_data_functions:
        file_ext = file_extension(function)
        urls.append(f"https://www.alphavantage.co/query?function={function}&symbol={stock.upper()}&apikey={keyAlphaVantage}&datatype={file_ext}")
    return urls       

def get_stocks_data(stock_symbol):
    urls = make_stock_urls(stock_symbol)
    for url in urls:
        if file_extension(url) == "csv":
            stock_data = pd.read_csv(url)
            stock_data = stock_data.set_index(pd.DatetimeIndex(stock_data['timestamp'].values))
        elif file_extension(url) == "json":
            with requests.Session() as s:
                data = s.get(url).content
                stock_overview = json.loads(data)
    return stock_data, stock_overview

def create_candlestick_chart(stock_dataframe, chart_time):
    # Create an interactive candlestick chart
    figure = go.Figure(
        data = [
            go.Candlestick(
                x = stock_dataframe.index,
                low = stock_dataframe['low'],
                high = stock_dataframe['high'],
                close = stock_dataframe['close'],
                open = stock_dataframe['open'],
                increasing_line_color = 'green',
                decreasing_line_color = 'red'
            )
        ]
    )
    figure.update_layout(
        title = chart_time,
        yaxis_title = "Stock Price USD ($)",
        xaxis_title = "Date"
        )
    return figure

if __name__ == "__main__":
    main()
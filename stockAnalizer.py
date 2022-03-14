import pandas as pd
import plotly.graph_objects as go
import json, csv
from stocks_data_collector import list_of_stocks
from stocks_data_collector import stock_data_functions



def main():
    stock_list = list_of_stocks()
    stock_data_file = f"{stock_list[0]}_{stock_data_functions[1]}.csv"
    stock_overview_file = f"{stock_list[0]}_{stock_data_functions[0]}.json"
    overview_data = {}

    with open(stock_overview_file, mode='r') as overview_file:
        overview_data.update(json.load(overview_file))
    stock_dataframe = pd.read_csv(stock_data_file)

    #setting timestamp as index of the dataframe
    stock_dataframe = stock_dataframe.set_index(pd.DatetimeIndex(stock_dataframe['timestamp'].values))

    print('')
    print("Stock Symbol:",overview_data["Symbol"],"\n")
    print("Description:",overview_data["Description"],"\n")
    print("Address:",overview_data["Address"],"\n")

    create_candlestick_chart(stock_dataframe, overview_data["Name"])

def create_candlestick_chart(stock_dataframe, stock_name):
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
    # figure.update_layout(xaxis_rangeslider_visible = False)
    figure.update_layout(
        title = stock_name,
        yaxis_title = "Stock Price USD ($)",
        xaxis_title = "Date"
        )
    figure.show()

if __name__ == "__main__":
    main()
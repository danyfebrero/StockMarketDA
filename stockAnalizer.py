import pandas as pd
import plotly.graph_objects as go
import json, csv, subprocess

from scipy.__config__ import show
from stocks_data_collector import list_of_stocks
from stocks_data_collector import stock_data_functions
import keys

menu_options = {
    1: 'Find Symbol',
    2: 'Last Symbol Searched',
    3: 'Change API Key',
    4: 'Exit',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def change_api_key():
    keys.remove_key_file()
    keys.get_key()

def get_stock_on_cache():
    show_symbol_info(True)

def find_symbol():
    show_symbol_info(False)

def show_symbol_info(cache):
    # Getting the stocks on cache
    stock_list = list_of_stocks(cache)
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
    figure.update_layout(
        title = stock_name,
        yaxis_title = "Stock Price USD ($)",
        xaxis_title = "Date"
        )
    figure.show()

if __name__ == "__main__":
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
            subprocess.call(["clear"]) 
            find_symbol()
            input("Press Enter to continue...")
        elif option == 2:
            subprocess.call(["clear"]) 
            get_stock_on_cache()
            input("Press Enter to continue...")
        elif option == 3:
            subprocess.call(["clear"]) 
            change_api_key()
            input("Press Enter to continue...")
        elif option == 4:
            subprocess.call(["clear"]) 
            print('Thanks you!')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')
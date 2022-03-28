from os import stat
import pandas as pd
import plotly.graph_objects as go
import json, csv, subprocess
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

    try:
        #setting timestamp as index of the dataframe
        stock_dataframe = stock_dataframe.set_index(pd.DatetimeIndex(stock_dataframe['timestamp'].values))

        print('')
        print(overview_data["Symbol"])
        print(overview_data["Name"])
        
        print(f"${stock_dataframe.close[0]}","\n")

        print("Description:\n",overview_data["Description"],"\n")
        print("Address:",overview_data["Address"],"\n")
        intrinsic_value = float(overview_data["EPS"]) * float(overview_data["PERatio"])
        print(f"Intrinsic value: {intrinsic_value}")

        print("Stats:\n")
        stats = stock_dataframe.iloc[0]
        print("Last update:", stats['timestamp'],"\n")
        stats = stats[['open','high','low','close','volume']]
        stats["52WeekHigh"]= overview_data["52WeekHigh"]
        stats["52WeekLow"]= overview_data["52WeekLow"]
        stats["PE/Ratio"]= overview_data["PERatio"]
        stats["DividendPerShare"]= overview_data["DividendPerShare"]

        print(stats.to_string(),"\n")

        create_candlestick_chart(stock_dataframe, overview_data["Name"])
    except KeyError:
        if len(overview_data) == 0:
            print("Invalid stock symbols, please try again.")
        else:
            print("You exceeded the usage/frequency limits: 5 API requests per minute and 500 requests per day.")

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
            
        elif option == 2:
            subprocess.call(["clear"]) 
            get_stock_on_cache()
            
        elif option == 3:
            subprocess.call(["clear"]) 
            change_api_key()
            
        elif option == 4:
            subprocess.call(["clear"]) 
            print('Thanks you!')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')
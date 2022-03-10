import pandas as pd
import mpl_finance as mpf
import matplotlib
from stocks_data_collector import list_of_stocks
from stocks_data_collector import stock_data_functions

def main():
    stock_list = list_of_stocks()
    file_name = f"{stock_list[0]}_{stock_data_functions[1]}.csv"
    data = pd.read_csv(file_name)
    print(data.info())
    
if __name__ == "__main__":
    main()
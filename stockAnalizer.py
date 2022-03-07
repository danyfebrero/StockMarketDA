from dataCollector import LoadStockData
import pandas as pd
import datetime, json
import matplotlib.pyplot as plt

def main():
    loaded_data = LoadStockData()
    stock_info_df = pd.DataFrame.from_dict(loaded_data["Meta Data"], orient="index")
    stock_statistics_df = pd.DataFrame.from_dict(loaded_data["Monthly Time Series"], orient="index")
    
    print(stock_info_df,"\n")
    print(stock_statistics_df.iloc[:5,0:])
    #print(stock_statistics_df.iloc[:5,2:3])
    #stock_statistics_df.iloc[:5,2:3].plot()
    #plt.show
    #print(stock_statistics_df)

if __name__ == "__main__":
    main()
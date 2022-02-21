from dataCollector import LoadStockData

def main():
    stock = LoadStockData()
    dates = stock["Monthly Time Series"]
    for eachDate in dates:
        print(dates[eachDate]["4. close"])
        print(dates[eachDate]["1. open"],"\n")

if __name__ == "__main__":
    main()
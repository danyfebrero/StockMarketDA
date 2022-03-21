# StockMarketDA
Stock Market Analyzer for Code Louisville
In this project, I create an interactive stock visualization website with Python/Flask and Alpha Vantage APIs. 

## GitHub repository
https://github.com/danyfebrero/StockMarketDA

## Requirements
Create an Alpha Vantage API key for free at https://www.alphavantage.co/support/#api-key)
     
## Description
The project is comprised of the following sections:
* Dependencies and set up project
* Data model
* Frontend UI
* Backend logic
* Set up Flask URL routing
* Run the web application locally

## Dependencies and set up project
We recommend Python 3.9.7 or higher. If you do not yet have Python installed, please follow the download instructions on the official python.org website.

Once you have Python installed in your environment, please use your command line interface to install the following Python libraries:
 * Create a virtual enviroment 
    python3 -m venv venv
    source ./venv/bin/activate
 * installing packages
    pip instal -r requirement.txt

## How to run the project
### for command line run:
    python3 stockAnalizer.py

### for UI (not ready yet)
#### For mac and linux:
 * Location of module containing our app:
    export FLASK_APP=app.py

* Enable developers features like debugging:
    export FLASK_ENV=development

* Run the application:
    flask run

#### For windows:
* Location of module containing our app:
        set FLASK_APP=flashcards.py

* Enable developers features like debugging:
    set FLASK_ENV=development

* Run the application:
    flask run

## Data model (stock_data_collector.py)

 * Created a dictionary and lists, I did populate it with several values, retrieve at least one value, and use it in my program.
 * Created and call at least 3 functions or methods, at least one of which return a value that is used somewhere else in my code
 * Calculated and displayed data based on an external factor.
 * Analyzed text and display information about it 
 * Read data from an external file, such as text, JSON, CSV, etc, and use that data in your application.
 * Connect to an external/3rd party API and read data into your app
 * Implement a log that records errors, invalid inputs, or other important events and writes them to a text file.


## Frontend UI (app.py)
 * Visualized data in a graph, chart, or other visual representation of data.
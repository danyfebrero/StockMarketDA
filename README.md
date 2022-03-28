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
 
 * To list all the virtual environments (if using the anaconda distribution):

       conda info --envs 

## How to run the project
### for command line run:
    python3 stockAnalizer.py

### for UI
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

## FEATURE LIST:
### Category 1: Python Programming Basics:
 * Implemented a “master loop” console application where the user can repeatedly enter commands/perform actions, including choosing to exit the program. (stockAnalizer.py >> into dunder name funtion)	
 * Created a dictionary and lists, I did populate it with several values, retrieve at least one value, and use it in my program.
 * Created and call at least 3 functions or methods, at least one of which return a value that is used somewhere else in my code
 * Calculated and displayed data based on an external factor. (stockAnalizer.py and app.py)
 * Analyzed text and display information about it (stockAnalizer.py and app.py)

### Category 2: Utilize External Data:
 * Connect to an external/3rd party API and read data into your app (stock_data_collector.py and model.py)
 * Read data from an external file, such as text, JSON, CSV, etc, and use that data in your application.

### Category 3: Data Display
 * Visualized data in a graph, chart, or other visual representation of data. (stockAnalizer.py and app.py)
 * Display data in tabular form (stockAnalizer.py)

### Category 4: Best Practices
 * The program utilize a virtual environment and document library dependencies in a requirements.txt file.

### “STRETCH” FEATURE LIST:
* Use pandas, matplotlib, and/or numpy to perform a data analysis project. Ingest 2 or more pieces of data, analyze that data in some manner, and display a new result to a graph, chart, or other display.
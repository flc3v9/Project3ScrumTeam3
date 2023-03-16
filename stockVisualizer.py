# this code requires pip pygal, lxml, and requests
import pygal, lxml, requests
from datetime import datetime

# Write our functions
def getSymbol():
    #QY73AL7RJZDQESXX
    symbol = input("Enter the stock symbol for the company you want data for: ")
    #if(symbol != stock api data)
    #{print("Please put in a valid stock ID")}
    #else{return symbol}
    return symbol

def getChartType():
    return

def getTimeSeries():
    print('Select the Time Series of the chart you want to Generate:\n------------------------------------')
    print('1. Intraday\n2. Daily\n3. Weekly\n4.Monthly')
    choice = ""
    while True:
        timeSeriesOption = int(input('Enter time series option(1, 2, 3, 4): '))
        if (timeSeriesOption == 1):
            choice = "TIME_SERIES_INTRADAY"
            return choice
        elif (timeSeriesOption == 2):
            choice = "TIME_SERIES_DAILY_ADJUSTED"
            return choice
        elif (timeSeriesOption == 3):
            choice = "TIME_SERIES_WEEKLY"
            return choice
        elif (timeSeriesOption == 4):
            choice = "TIME_SERIES_MONTHLY"
            return choice
        else:
            print('You have not chosen a valid option. Please only enter values between 1-4.')

def getDate(dateType):
    while True:
        strDate = input(f"Enter the {dateType} date in YYYY-MM-DD format:\n")
        
        # check format
        format = "%Y-%m-%d"
        try:
            date = datetime.strptime(strDate, format)
            break
        except:
            print("Please use the YYYY-MM-DD format.\n")
            continue
    return date

def generateGraph(symbol, chart, timeSeries, beginDate, endDate):
    inputdata = [symbol, chart, timeSeries, beginDate, endDate]
    if (inputdata[2] == 'INTRADAY'):
        # this will depend upon the user's date choice. unfortunately video does not explain this so we will have to ask him if there is a defaul intraday interval or if not. if there is not, user will have to be able to choose this as well.
        # if does have intraday, will have to add this to data variable as part of api connection
        pass
    # this is gonna be the biggest challenge as it will require us to convert the beginning and end date input, split this accordingly by time series, and then plot all of the split data in to a graph. I would highly recommend a list/array of some sort to store the data and then put that into the graph

    # will likely use requests here like as shows
    data = {'FUNCTION':'inputfromtimeseries', 'SYMBOL':'inputfromsybolfunction', 'APIKEY':'QY73AL7RJZDQESXX'}
    requestedData = requests.get('https://www.alphavantage.co/query?',params=data)
    # then you would use requestedData and parse thru the dates you specified in date functions; THIS IS WHAT WILL BE PUT INTO THE GRAPH

    # you would write a function like match data where begin date is x and end date is y and then put that into array
        # you will have to figure out way to parse thru json file. this is likely where you would use postman for help and you would use json and you would parse thru this by figuring out how to select specific date

    if (inputdata[1] == 'line'):
        # USE PYGAL HERE, would likely create type_chart.add loop for each split in time series (ex. you requested 30 days of daily information, you must split this daily into different adds)
        pass
    else:
        # USE PYGAL BAR HERE
        pass

    return


# Call our functions
def main():
    try:
        getSymbol()
        getChartType()
        getTimeSeries()
        getDateRange()
        generateGraph()
    except Exception as error:
        print(f"Something went wrong with the symbol. {str(error)}")

main()
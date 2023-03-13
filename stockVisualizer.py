# this code requires pip pygal, lxml, and requests
import pygal, lxml, requests
from datetime import datetime


# API
    # for these, you will want to use the link format. we might have to see how to connect these

# Write our functions
def getSymbol():
    return

def getChartType():
    return

def getTimeSeries():
    return

def getDateRange():
    while True:
        startDate = getDate("start")
        print("")
        endDate = getDate("end")

        if(startDate < endDate):
            break
        else:
            print("\nError: Start date cannot be later than End date. Enter the dates again.\n")
            continue
    return startDate, endDate

def getDate(dateType):
    while True:
        strDate = input(f"Enter the {dateType} date (YYYY-MM-DD): ")
        
        # check format
        format = "%Y-%m-%d"
        try:
            date = datetime.strptime(strDate, format)
            break
        except:
            print("Please use the YYYY-MM-DD format.\n")
            continue
    return date

def generateGraph(symbol, chart, timeSeries, startDate, endDate):
    inputData = [symbol, chart, timeSeries, startDate, endDate]
    if (inputData[2] == 'INTRADAY'):
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

    if (inputData[1] == 'line'):
        # USE PYGAL HERE, would likely create type_chart.add loop for each split in time series (ex. you requested 30 days of daily information, you must split this daily into different adds)
        pass
    else:
        # USE PYGAL BAR HERE
        pass

    return

def main():
    while True:
        # title
        print("Stock Data Visualizer")
        print("-------------------------\n")
        
        # run program
        symbol = getSymbol()
        chart = getChartType()
        timeSeries = getTimeSeries()
        startDate, endDate = getDateRange()
        generateGraph(symbol, chart, timeSeries, startDate, endDate)
        
        # run again?
        run_again_input = input("\nWould you like to view more stock data? (y/n): ")
        if (run_again_input == "y"):
            print("\n")
            continue
        else:
            print("\nOkay, thank you for using this program.")
            break

main()
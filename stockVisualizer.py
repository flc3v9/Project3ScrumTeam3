# this code requires pip pygal, lxml, and requests
import pygal, lxml, requests
from datetime import datetime

def getSymbol():
    symbol = input("Enter the stock symbol for the company you want data for: ")
    return symbol

def getChartType():
    print('Chart Type\n------------------------------------')
    print('1. Bar\n2. Line')
    choice = ""
    while True:
        chartTypeOption = int(input('Enter chart type you want (1, 2): '))
        if (chartTypeOption == 1):
            choice = "Bar"
            return choice
        elif (chartTypeOption == 2):
            choice = "Line"
            return choice
        else:
            print('You have not chosen a valid option. Please only enter values 1 or 2.')

def getTimeSeries():
    print('Select the Time Series of the chart you want to Generate:\n------------------------------------')
    print('1. Intraday\n2. Daily\n3. Weekly\n4. Monthly')
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

def getData(timeSeries, symbol):
    # populate the query parameters
    queryData = {'function': '', 'symbol': '', 'interval': '', 'apikey': ''}
    queryData['function'] = timeSeries
    queryData['symbol'] = symbol
    queryData['apikey'] = "QY73AL7RJZDQESXX"
    if (timeSeries == "TIME_SERIES_INTRADAY"):
        queryData['interval'] = "15min"

    # request the data from alpha vantage
    alphavantageRequest = requests.get('https://www.alphavantage.co/query', params=queryData)
    print(alphavantageRequest.url)

    # check if request successfull
    if alphavantageRequest.status_code == 200:
        # turn Response object into a python dictionary
        stocksDictionary = alphavantageRequest.json()
        return stocksDictionary
    else:
        print("Error: Request failed")

def generateGraph(symbol, timeSeries, chart, stocksDictionary, startDate, endDate):
    # get the name of the data for that time series ex. 'Monthly Time Series'
    timeSeriesName = list(stocksDictionary)[1]

    # create a reference to the time series data
    timeSeriesData = stocksDictionary[timeSeriesName]

    # name graph
    displayStartDate = startDate.strftime("%Y/%m/%d")
    displayEndDate = endDate.strftime("%Y/%m/%d")
    graphTitle = f"Stock Data for {symbol}: {displayStartDate} to {displayEndDate}"

    # create graph based on selected chart
    if (chart == "Line"):
        generateLineGraph(timeSeries, timeSeriesData, startDate, endDate, graphTitle)
    if (chart == "Bar"):
        generateBarChart(timeSeries, timeSeriesData, startDate, endDate, graphTitle)

def generateLineGraph(timeSeries, timeSeriesData, startDate, endDate, graphTitle):
    # list the graph lines
    graphLines = ["1. open", "2. high", "3. low", "4. close"]

    # creating line graph
    lineGraph = pygal.Line(title=graphTitle, x_label_rotation=45, x_value_formatter=lambda dt: dt.strftime('%Y-%m-%d %H:%M:%S'))

    # loop through each line
    for line in graphLines:
        # create list of data points for the line
        dataPoints = list()
        x_labels = list()
        # loop through the timeSeriesData (objects) to populate dataPoints list
        for date, values in timeSeriesData.items():
            # turn the date string into a datetime object
            if (timeSeries == "TIME_SERIES_INTRADAY"):
                date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
            else:
                date = datetime.strptime(date, "%Y-%m-%d")
            # find objects based on date range
            if date > startDate and date < endDate:
                # add date to x-axis label list (assign x-coordinate the date)
                if (timeSeries == "TIME_SERIES_INTRADAY"):
                    x_labels.insert(0, date.strftime("%Y/%m/%d %H:%M:%S"))
                else:
                    x_labels.insert(0, date.strftime("%Y/%m/%d"))
                # assign y-coordinate it's value based on the current key (line name)
                y = float(values[line])
                # add the y-coordinate to the list of data points
                dataPoints.append(y)
        # add the line with all of the data points
        lineGraph.add(line, dataPoints)
    
    # set x-axis labels
    lineGraph.x_labels = x_labels

    # open graph in browser
    lineGraph.render_in_browser()

def generateBarChart(timeSeries, timeSeriesData, startDate, endDate, graphTitle):
    # list the chart labels
    chartLabels = ["1. open", "2. high", "3. low", "4. close"]

    # creating bar chart
    barChart = pygal.Bar(title=graphTitle, x_label_rotation=45)

    # loop through each label
    for label in chartLabels:
        x_labels = list() # dates in the range
        dataPoints = list() # values per label (date is determined by x-labels)
        # loop through the timeSeriesData (objects) to popoulate dataPoints list
        for date, values in timeSeriesData.items():
            # turn the date string into a datetime object
            if (timeSeries == "TIME_SERIES_INTRADAY"):
                date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
            else:
                date = datetime.strptime(date, "%Y-%m-%d")
            # find objects based on date range
            if date > startDate and date < endDate:
                # add date to x-axis label list
                if (timeSeries == "TIME_SERIES_INTRADAY"):
                    x_labels.insert(0, date.strftime("%Y/%m/%d %H:%M:%S"))
                else:
                    x_labels.insert(0, date.strftime("%Y/%m/%d"))
                # add value to data point list
                y = float(values[label])
                dataPoints.append(y)
        # add data to chart
        barChart.add(label, dataPoints)
    
    # set x-axis labels
    barChart.x_labels = x_labels
    
    # open graph in browser
    barChart.render_in_browser()

# Call our functions
def main():
    while True:
        # title
        print("Stock Data Visualizer")
        print("-------------------------\n")

        # run program
        try:
            symbol = getSymbol()
            
            print("")
            chart = getChartType()
            
            print("")
            timeSeries = getTimeSeries()
            
            print("")
            startDate, endDate = getDateRange()
            
            print("")
            stocksDictionary = getData(timeSeries, symbol)
            generateGraph(symbol, timeSeries, chart, stocksDictionary, startDate, endDate)
        except Exception as error:
            print("Something went wrong with the symbol entered. Please try again.\n")
            continue

        # run again?
        run_again_input = input("\nWould you like to view more stock data? (y/n): ")
        if (run_again_input == "y"):
            print("\n")
            continue
        else:
            print("\nOkay, thank you for using this program.")
            break

main()
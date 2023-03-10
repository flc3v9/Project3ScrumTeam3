# this is the function for the time series python function

# create menu option

def getTimeSeries():
    print('Select the Time Series of the chart you want to Generate:\n------------------------------------')
    print('1. Intraday\n2. Daily\n3. Weekly\n4.Monthly')
    choice = ""
    while True:
        timeSeriesOption = input('Enter time series option(1, 2, 3, 4):')
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

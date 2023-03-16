from alpha_vantage.timeseries import TimeSeries

ts = TimeSeries(key='QY73AL7RJZDQESXX')


def SelectTimeSeries():

    print("Select the Time Series of the chart you want to Generate:")
    print('1. Intraday\n2. Daily\n3. Weekly\n4.Monthly')

    TimeSeriesOption = int(input('Enter time series option(1, 2, 3, 4): '))

    monthlydata = ts.get_monthly(TimeSeriesOption)
  

    while True:

        if (TimeSeriesOption == 1):
            intradata = ts.get_intraday(TimeSeriesOption)
            return intradata
        
        elif (TimeSeriesOption == 2):
            dailydata = ts.get_daily(TimeSeriesOption)
            return 
        
        elif (TimeSeriesOption == 3):
            weeklydata = ts.get_weekly(TimeSeriesOption)
            return 
        
        elif (TimeSeriesOption == 4):
            monthlydata = ts.get_monthly(TimeSeriesOption)

            return monthlydata
        
        else:
            print('You have not chosen a valid option. Please only enter values between 1-4.')

SelectTimeSeries()
from src import *

crawler = Crawler()
calender = Calender()

# start year
startYear = 2016
# start month
startMonth = 1
# end year
endYear = 2017
# end month
endMonth = 2


while startYear < (endYear+1):
    while startMonth < 13:
        month = calender.getDayInMonth(startYear, startMonth)
        for day in month:
            crawler.getURLData(int(day))
        if startMonth == endMonth and startYear == endYear:
            break
        startMonth += 1
    startMonth = 1
    startYear += 1



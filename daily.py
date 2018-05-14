from src import *

crawler = Crawler()
calender = Calender()

# start year
startYear = 2018
# start month
startMonth = 3
# end year
endYear = 2018
# end month
endMonth = 3


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



from src import *

crawler = Crawler()
calender = Calender()

# start year
startYear = 2006
# start month
startMonth = 9
# end year
endYear = 2007
# end month
endMonth = 5


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



from src import *

crawl = Crawler()
cal = Calender()

year = 2013
finalYear = 2013
totalMonths = 12
startMonth = 4

while year < (finalYear+1):
    while startMonth < 5:
        y = cal.getDayInMonth(year, startMonth)
        for i in y:
            crawl.getURLData(int(i))
        startMonth += 1
    startMonth = 1
    year += 1



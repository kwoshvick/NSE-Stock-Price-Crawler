from src import *

crawl = Crawler()
cal = Calender()

year = 2017
finalYear = 2017
totalMonths = 12
startMonth = 1

while year < (finalYear+1):
    while startMonth < 2:
        y = cal.getDayInMonth(year, startMonth)
        for i in y:
            crawl.getURLData(int(i))
        startMonth += 1
    startMonth = 1
    year += 1



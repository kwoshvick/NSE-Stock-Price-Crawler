from src import *

crawl = Crawler()
cal = Calender()

year = 2010
finalYear = 2010
totalMonths = 12
startMonth = 12

while year < (finalYear+1):
    while startMonth < 13:
        y = cal.getDayInMonth(year, startMonth)
        for i in y:
            crawl.getURLData(int(i))
        startMonth += 1
    startMonth = 1
    year += 1



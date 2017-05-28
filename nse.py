from src import *
import calendar

crawl = Crawler()
cal = Calender()

# date = https://live.mystocks.co.ke/price_list/20160501

year = 2006
finalYear = 2006
totalMonths = 12
startMonth = 9

while year < (finalYear+1):
    while startMonth < 13:
        y = cal.getDayInMonth(year, startMonth)
        for i in y:
            crawl.getURLData(int(i))
        startMonth += 1
    startMonth = 1
    year += 1











# c = calendar.calendar(2006)
#
# print(c)

# y = cal.getDayInMonth(2006,2)
# for i in y:
#     crawl.getURLData(int(i))
#
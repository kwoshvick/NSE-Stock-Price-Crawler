import os
import shutil
from src import *

crawler = Crawler()
calender = Calender()
formatter = FormatData()

# start year
startYear = 2022
# start month
startMonth = 1
# end year
endYear = 2022
# end month
endMonth = 4

print("Preparing Daily Data")
while startYear < (endYear+1):
    print("Year",startYear)
    while startMonth < 13:
        print("Month:",startMonth)
        month = calender.getDayInMonth(startYear, startMonth)
        for day in month:
            crawler.getURLData(int(day))
        if startMonth == endMonth and startYear == endYear:
            break
        startMonth += 1
    startMonth = 1
    startYear += 1


for folder in ['monthly','yearly','company']:
    shutil.rmtree('data/'+folder,ignore_errors=True, onerror=None)
    os.mkdir('data/'+folder)


pathDaily = 'data/daily/'
pathYearly = 'data/yearly/'
pathMonthly = 'data/monthly/'
pathCompany = 'data/company/'

# create monthly data
print("Preparing Monthly Data")
formatter.getMonthlyData(pathDaily, pathMonthly)

# create yearly data
print("Preparing Yearly Data")
formatter.getYearlyData(pathMonthly, pathYearly)

# create company data
print("Preparing Company Data")
formatter.getCompanyData(pathYearly, pathCompany)

print("Process Completed !!")




import os
import shutil
from src import *

crawler = Crawler()
calender = Calender()
formatter = FormatData()

# start year
startYear = 2006
# start month
startMonth = 11
# end year
endYear = 2020
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


for folder in ['monthly','yearly','company']:
    shutil.rmtree('data/'+folder,ignore_errors=True, onerror=None)
    os.mkdir('data/'+folder)


pathDaily = 'data/daily/'
pathYearly = 'data/yearly/'
pathMonthly = 'data/monthly/'
pathCompany = 'data/company/'

# create monthly data
formatter.getMonthlyData(pathDaily, pathMonthly)

# create yearly data
formatter.getYearlyData(pathMonthly, pathYearly)

# create company data
formatter.getCompanyData(pathYearly, pathCompany)




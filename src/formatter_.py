import os
import csv

class FormatData():
    def __init__(self,inputPath,outputPath):
        self.inputpath = inputPath
        self.outputpath = outputPath
        self.yearsFolder = list()
        self.compute()

    def getYears(self):
        for years in os.listdir(self.inputpath):
            self.yearsFolder.append(years)
        sortedYearsFolder = sorted(self.yearsFolder)
        return sortedYearsFolder

    def getMonths(self,path):
        monthsFolder = list()
        for months in os.listdir(path):
            monthsFolder.append(months)
        sortedMonthsFolder = sorted(monthsFolder)
        return sortedMonthsFolder

    def getDays(self,path):
        daysFolder = list()
        for days in os.listdir(path):
            daysFolder.append(days)
        sortedDaysFolder = sorted(daysFolder)
        return sortedDaysFolder


    def compute(self):
        years = self.getYears()
        for year in years:
            monthlyPath = self.inputpath+str(year)+'/'
            months = self.getMonths(monthlyPath)
            for month in months:
                dailyPath = monthlyPath+str(month)+'/'
                days = self.getDays(dailyPath)
                for day in days:
                    csvPath = dailyPath+str(day)
                    self.monthlyCSV(csvPath,day)

    def monthlyCSV(self,dailyPath,fileName):
        with open(dailyPath, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
            for row in spamreader:
                date = fileName.strip('.csv')
                # append date to be the first element
                row.insert(0, date)
                file = open(self.outputpath + str(row[1]) + '.csv', 'a')
                writeFile = csv.writer(file, delimiter=',')
                # removes the code
                del row[1]
                # removes the company name
                del row[1]
                writeFile.writerows([row])
                file.close()

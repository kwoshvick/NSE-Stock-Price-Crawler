import os
import csv
from src.crawler_ import Crawler

class FormatData:
    def __init__(self):
        self.yearsFolder = list()
        self.crawler = Crawler()

    # returns the years,months, days and csv in the folder.
    # It depends on when its being referenced.
    def getDataInFolder(self,path):
        dataFolder = list()
        for data in os.listdir(path):
            dataFolder.append(data)
        sortedDataFolder = sorted(dataFolder)
        return sortedDataFolder

    # extract data from the csv
    def getMonthlyData(self,inputPath,outputPath):
        #return years in folder
        years = self.getDataInFolder(inputPath)
        for year in years:
            self.crawler.createFolder(outputPath + str(year))
            yearlyPath = inputPath+str(year)+'/'
            # returns months in a folder
            months = self.getDataInFolder(yearlyPath)
            for month in months:
                self.crawler.createFolder(outputPath + str(year)+'/'+str(month))
                monthlyPath = yearlyPath+str(month)+'/'
                # returns days in a folder
                days = self.getDataInFolder(monthlyPath)
                for day in days:
                    dailyCsvPath = monthlyPath+str(day)
                    self.monthlyCSV(dailyCsvPath, day,outputPath + str(year)+'/'+str(month)+'/')

    # saves the data in the relevant csv file
    def monthlyCSV(self, dailyPath, fileName, finalPath):
        with open(dailyPath, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
            for row in spamreader:
                date = fileName.strip('.csv')
                # append date to be the first element
                row.insert(0, date)
                file = open(finalPath + str(row[1]) + '.csv', 'a')
                writeFile = csv.writer(file, delimiter=',')
                # removes the code
                del row[1]
                # removes the company name
                del row[1]
                writeFile.writerows([row])
                file.close()


    # returns the years in the folder
    # def getYears(self):
    #     for years in os.listdir(self.inputpath):
    #         self.yearsFolder.append(years)
    #     sortedYearsFolder = sorted(self.yearsFolder)
    #     return sortedYearsFolder

    # returns the months in the folder
    # def getMonths(self,path):
    #     monthsFolder = list()
    #     for months in os.listdir(path):
    #         monthsFolder.append(months)
    #     sortedMonthsFolder = sorted(monthsFolder)
    #     return sortedMonthsFolder

    # returns the days csvs' in the folder
    # def getDays(self,path):
    #     daysFolder = list()
    #     for days in os.listdir(path):
    #         daysFolder.append(days)
    #     sortedDaysFolder = sorted(daysFolder)
    #     return sortedDaysFolder



    # saves the data in the relevant csv file
    # def monthlyCSV2(self, dailyPath, fileName, finalPath):
    #     with open(dailyPath, newline='') as csvfile:
    #         spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    #         for row in spamreader:
    #             file = open(finalPath + str(fileName), 'a')
    #             writeFile = csv.writer(file, delimiter=',')
    #             writeFile.writerows([row])
    #             file.close()

    # saves the data in the relevant csv file
    # def monthlyCSV3(self, dailyPath, fileName, finalPath):
    #     with open(dailyPath, newline='') as csvfile:
    #         spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    #         for row in spamreader:
    #             file = open(finalPath + str(fileName), 'a')
    #             writeFile = csv.writer(file, delimiter=',')
    #             writeFile.writerows([row])
    #             file.close()



    # extract data from the csv

    # def getData2(self, inputPath, outputPath):
    #     self.inputpath = inputPath
    #     self.outputpath = outputPath
    #     years = self.getYears()
    #     for year in years:
    #         self.crawler.createFolder(self.outputpath + str(year))
    #         yearlyPath = self.inputpath + str(year) + '/'
    #         months = self.getMonths(yearlyPath)
    #         for month in months:
    #             monthlyPath = yearlyPath + str(month) + '/'
    #             months = self.getDays(monthlyPath)
    #             for i in months:
    #                 csvPath = monthlyPath + str(i)
    #                 print(csvPath)
    #         #     for day in days:
    #         #         csvPath = dailyPath + str(day)
    #                 self.monthlyCSV2(csvPath, i, self.outputpath + str(year) + '/' )


    # def getData3(self, inputPath, outputPath):
    #     self.inputpath = inputPath
    #     self.outputpath = outputPath
    #     years = self.getYears()
    #     for year in years:
    #         # self.crawler.createFolder(self.outputpath + str(year))
    #         yearlyPath = self.inputpath + str(year) + '/'
    #         year = self.getDays(yearlyPath)
    #         for i in year:
    #             csvPath = yearlyPath + str(i)
    #             print(csvPath)
    #             self.monthlyCSV3(csvPath, i, self.outputpath + '/')
    #         # months = self.getMonths(yearlyPath)
    #         # for month in months:
    #         #     monthlyPath = yearlyPath + str(month) + '/'
    #         #     months = self.getDays(monthlyPath)
    #         #
    #         # #     for day in days:
    #         # #         csvPath = dailyPath + str(day)
    #         #         self.monthlyCSV2(csvPath, i, self.outputpath + str(year) + '/' )
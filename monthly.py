import os

import csv
fileName = '20061201.csv'
dailyPath = 'data/monthly/12/'+fileName
monthlyPath = 'data/monthly/'



with open(dailyPath, newline='') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
     for row in spamreader:
         date = fileName.strip('.csv')
         # append date to be the first element
         row.insert(0, date)
         file = open(monthlyPath + str(row[1]) + '.csv', 'a')
         writeFile = csv.writer(file, delimiter=',')
         writeFile.writerows([row])
         file.close()

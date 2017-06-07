import os
import csv

mypath = 'data/monthly/12/'
monthlyOutputPath = 'data/monthly/'
filesInFolder = list()
for csvFile in os.listdir(mypath):
    filesInFolder.append(int(csvFile.strip(".csv")))
# sort in ascending order
sortedFilesInFolder = sorted(filesInFolder)


for sortedFile in sortedFilesInFolder:
    fileName = str(sortedFile)+'.csv'
    dailyPath = mypath+fileName
    # save in csv
    with open(dailyPath, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in spamreader:
            date = fileName.strip('.csv')
            # append date to be the first element
            row.insert(0, date)
            file = open(monthlyOutputPath + str(row[1]) + '.csv', 'a')
            writeFile = csv.writer(file, delimiter=',')
            print(row)
            # removes the code
            del row[1]
            # removes the company name
            del row[1]
            writeFile.writerows([row])
            file.close()



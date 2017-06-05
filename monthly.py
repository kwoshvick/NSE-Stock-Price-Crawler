import csv
with open('data/monthly/12/20061201.csv', newline='') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
     for row in spamreader:
         print(row)
         # print(' '.join(row))
from os import listdir
from os.path import isfile, join
mypath = 'data/monthly/12/'
filesInFolder = list()
for csvFile in listdir(mypath):
    filesInFolder.append(int(csvFile.strip(".csv")))

m = sorted(filesInFolder)
print(m)
# onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
#
# print(onlyfiles)f.strip(".csv")
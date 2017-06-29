from src import *

inputPath = 'data/daily/'
outputPath = 'data/monthly/'

formatter = FormatData()
formatter.getData(inputPath, outputPath)


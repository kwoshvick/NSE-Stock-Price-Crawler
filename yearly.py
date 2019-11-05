from src import *

inputPath = 'data/monthly/'
outputPath = 'data/yearly/'

formatter = FormatData()
formatter.getYearlyData(inputPath, outputPath)
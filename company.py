from src import *

inputPath = 'data/yearly/'
outputPath = 'data/company/'

formatter = FormatData()
formatter.getCompanyData(inputPath, outputPath)
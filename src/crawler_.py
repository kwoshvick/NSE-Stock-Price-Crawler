import os
import csv
import logging
import datetime
import urllib.error as error
import urllib.request as rq
from bs4 import BeautifulSoup


class Crawler:
    def __init__(self):
        #log errors for pages not found
        logging.basicConfig(filename='errorlog/error.log', level=logging.ERROR)

    def getURLData(self,date):
        '''
                the list dailyShares contains all the companies shares of that day
                shareDetails list contains all the details of a particular company .i.e name, code , volume e.t.c
                shareElement list makes up the Share Details which makes up the dailyShares list
        '''
        self.dailyShares = list()
        self.date = str(date)
        self.createFolder('data/daily/'+self.date[0:4])
        url = "https://live.mystocks.co.ke/price_list/" + self.date
        try:
            html = rq.urlopen(url).read()
            self.soup = BeautifulSoup(html, "lxml")
            self.extractURLData()
        except error.HTTPError as e:
            now = datetime.datetime.now()
            errorMessage = str(now)+' - '+str(e)+' Date: '+str(self.date)
            print('Please check error log file in errorlog directory')
            logging.error(errorMessage)

    # Extract the data from the page requested
    def extractURLData(self):
        table = self.soup.find("table", {"class": "tblHoverHi"})
        for row in table.findAll("tr"):
            shareDetails = list()
            shareElements = list()
            for element in row.findAll("td"):
                # the share categories i.e banking, manufacturing
                for heading in element.findAll("h3"):
                    _heading = heading.string
                # the share company name
                for item in element.findAll("a"):
                    shareElements.append(item.string)
                # the shares details i.e price,volume
                if element.string != heading.string:
                    shareElements.append(element.string)
            # removes empty and None arrays, clean up from html extracted data
            if (shareElements != [] and len(shareElements) > 1):
                # code
                shareDetails.append(shareElements[0])
                # name
                shareDetails.append(shareElements[1])
                # lowest price
                if shareElements[5] == None:
                    shareDetails.append(shareElements[5])
                else:
                    shareDetails.append(float(shareElements[5].replace(',', '')))
                # highest price
                if shareElements[6] == None:
                    shareDetails.append(shareElements[6])
                else:
                    shareDetails.append(float(shareElements[6].replace(',', '')))
                # price
                if shareElements[7] == None:
                    shareDetails.append(shareElements[7])
                else:
                    shareDetails.append(float(shareElements[7].replace(',', '')))
                # previous day's price
                if shareElements[8] == None or shareElements[8] == '-':
                    shareDetails.append(shareElements[8])
                else:
                    shareDetails.append(float(shareElements[8].replace(',', '')))
                # volume
                if (shareElements[12] == None) or (shareElements[12] == '-'):
                    shareDetails.append(shareElements[12])
                else:
                    shareDetails.append(str(shareElements[12].replace(',', '')))
                self.dailyShares.append(shareDetails)
        self.saveCSV()

    # creates a folder for either the year or month if it doesnt exist
    def createFolder(self,path):
        folder = os.path.isdir(path)
        if folder is False:
            os.mkdir(path)

    # saves the data extracted in a csv
    def saveCSV(self):
        year = self.date[0:4]
        month = self.date[4:6]
        path = 'data/daily/'+str(year)+'/'+month+'/'
        folder = os.path.isdir(path)
        if folder == False:
            os.mkdir(path)
        myFile = open(path+str(self.date)+'.csv', 'w')
        writeFile = csv.writer(myFile, delimiter=';')
        writeFile.writerows(self.dailyShares)
        myFile.close()
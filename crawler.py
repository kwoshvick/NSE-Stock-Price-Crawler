import urllib.request as rq
from bs4 import BeautifulSoup

#https://live.mystocks.co.ke/price_list/20170519
# url = input('Enter ')
url = "https://live.mystocks.co.ke/price_list/20170519"
html = rq.urlopen(url).read()
soup = BeautifulSoup(html,"lxml")
'''
the list dailyShares contains all the companies shares of that day
shareDetails list contains all the details of a particular company .i.e name, code , volume e.t.c
shareElement list makes up the Share Details which makes up the dailyShares list
'''

dailyShares = list()

table = soup.find("table", { "class": "tblHoverHi"})
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
    if(shareElements !=[] and len(shareElements)>1 ):
        #code
        shareDetails.append(shareElements[0])
        #name
        shareDetails.append(shareElements[1])
        #lowest price
        shareDetails.append(shareElements[5])
        #highest price
        shareDetails.append(shareElements[6])
        #price
        shareDetails.append(shareElements[7])
        #volume
        shareDetails.append(shareElements[12])
        dailyShares.append(shareDetails)

print(dailyShares)

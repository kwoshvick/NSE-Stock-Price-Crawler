
# NSE-Stock-Crawler

This is a web crawler for Nairobi Stock Exchange **(NSE)** Share prices since its digitization on 11 th September 2006.
The data crawled can be found in the `data` folder.

**Setup**

- Install python3 and pip3 installed
 ```sh
   pip3 install -r requirements.txt
  ``` 
  - To install the python3 dependencies.


**Data Format in the csv's**

* *Daily csv Format*
    * Each csv contains daily prices for all the companies for that day.
    *  Code | Name | Lowest Price of the day | Highest Price of the day | Closing Price | Volume Traded

* *Monthly & Yearly csv Format*
    * Each csv contains a particulars company prices for the month/ year
   * Date | Lowest Price of the day | Highest Price of the day | Closing Price | Volume Traded

The `data` folder has 3 folders inside:
* `Daily` folder
Has all nse daily prices ordered by year and months
* `Monthly` folder
All daily data put in a single csv for that month ordered by company code name.
* `Yearly` folder
All monthly data put in a single csv for that year.

All errors *404* errors for pages not found can be found in the `errorlog` folder in the **error.log**

**NB** Unable to remove the following holidays as of now because they are dynamic
 - Eid al Adha (was gazetted in Kenya as of September 2016)
 
 - Eid Fitr 
 
# Contribution 

If you have any additions fork this project repo, make changes on your clone and make a Pull Request. 
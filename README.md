
# NSE Stock Price Crawler

This is a web crawler for Nairobi Security Exchange **(NSE)** Share prices since its digitization on 11<sup>th</sup> September 2006 to 31<sup>st</sup> August 2020.
The data crawled can be found in the `data` folder.

**Setup**

- Install python3 and pip3 installed
 ```sh
   pip3 install -r requirements.txt
  ``` 
  - To install the python3 dependencies.


**Data Format in the csv**

* *Daily csv Format*
    * Each csv contains daily prices for all the companies for that day.
    * Code | Name | Lowest Price of the Day | Highest Price of the Day | Closing Price | Previous Day Closing Price | Volume Traded

* *Monthly , Yearly and Company csv Format*
    * Each csv contains a particulars company prices for the month/ year
   * Date | Lowest Price of the Day | Highest Price of the Day | Closing Price | Previous Day Closing Price | Volume Traded

The `data` folder has 4 folders inside:
* `Daily` folder
Has all NSE daily prices ordered by year and months
* `Monthly` folder
All daily data put in a single csv for that month ordered by company code name.
* `Yearly` folder
All monthly data put in a single csv for that year.
* `Company` folder
All yearly data put in a single csv for that company.


All errors *404* errors for pages not found can be found in the `errorlog` folder in the **error.log**

**NB** Unable to remove the following holidays as of now because they are dynamic
 - Eid al Adha (was gazetted in Kenya as of September 2016)
 
 - Eid Fitr 
 
 
**Usage**

- To run the crawler
``` sh 
python3 getData.py
```


**getData file**

- Set the following input
    - Start month
    - Start year
    - End month
    - End Year 

- The script also does the following:

    - The script crawls the data given the start dates and end dates.
                It gets data from [mystocks website](https://live.mystocks.co.ke/) , credits to them and saves them under the `data/daily/` folder.
                
    - It gets each company's data from the daily csvs. It creates a csv for each company and saves the monthly share prices of that company. The data is stored in the `data/monthly/` folder.
                  
    - It gets each company's data from the monthly csvs. It creates a csv for each company and saves the yearly share prices of that company. The data is stored in the `data/yearly/` folder.
                  
    - It gets each company's data from the yearly csvs. It creates a csv for each company and saves the company's share prices for the period specified. The data is stored in the `data/company/` folder.



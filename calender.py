import calendar
import time
from dateutil.parser import parse
calendar.setfirstweekday(calendar.SUNDAY)

# print(calendar.Calendar.itermonthdates(2017,5))

import calendar

cal = calendar.Calendar()
for x in cal.itermonthdates(2016, 5):
    pr
    # conv = time.strptime(x, "%a %b %d %Y")
    # print(time.strftime("%d/%m/%Y", conv))

    # y = x.replace('-','/')
    # print(y)

    # from_date = "Mon Feb 15 2010"
    # >> > import time
    # >> > conv = time.strptime(from_date, "%a %b %d %Y")
    # >> > time.strftime("%d/%m/%Y", conv)
    # '15/02/2010'
import calendar
import datetime
from dateutil.easter import *

class Calender:
    def __init__(self):
        calendar.setfirstweekday(calendar.MONDAY)
        self.calendar = calendar.Calendar()
        # add one day
        self._1daymore = datetime.timedelta(days=+1)
        # New Year's Day 1st January
        # Labour Day 1st May
        # Madaraka Day* 1st June
        # Mashujaa Day* 20th October
        # Jamhuri (Independence) Day* 12th December
        # Christmas Day 25th December
        # Boxing Day 26th December
        self.publicHolidays = {1: ['01'], 5: ['01'], 6: ['01'], 10: ['20'], 12: ['12', '25', '26']}

    # Returns days of that month
    def getDayInMonth(self,year,month):
        weekdays = list()
        self.month = month
        self.year = year
        for date in self.calendar.itermonthdates(year,month):
            newDate = datetime.datetime.strptime(str(date), '%Y-%m-%d').strftime('%Y%m%d')
            weekday = self.isWeekday(newDate)
            if weekday:
                if int(newDate[4:6]) == month:
                    weekdays.append(newDate)
                    self._strMonth = newDate[4:6]

        tradingDays = self.holiday(weekdays)
        print(tradingDays)
        exit()
        #return tradingDays

    # removes the weekends from the days of the month
    def isWeekday(self,date):
        day = calendar.weekday(int(date[0:4]),int(date[4:6]),int(date[6:8]))
        if day < 5:
            return True
        else:
            return False

    # removes a monday from the list if the holiday is on a Sunday
    def isHolidayOnSunday(self,day):
        date = datetime.datetime.strptime(str(day), '%Y%m%d').strftime('%Y-%m-%d')
        splitDate = date.split('-')
        whichDay = calendar.weekday(int(splitDate[0]), int(splitDate[1]), int(splitDate[2]))
        if whichDay == 6: # if Sunday
            newdate = datetime.datetime.strptime(date, '%Y-%m-%d').date()
            newHoliday= newdate + self._1daymore
            newHolidayDate = datetime.datetime.strptime(str(newHoliday), '%Y-%m-%d').strftime('%Y%m%d')
            return newHolidayDate
        else:
            return day

    # removes the holidays from the days of the month
    def holiday(self,monthDays):
        easterDays = list()
        if self.month in self.publicHolidays.keys():
            days = self.publicHolidays.__getitem__(self.month)
            for day in days:
                newDate = str(self.year) + str(self.month) + day
                newDay = self.isHolidayOnSunday(newDate)
                if newDay in monthDays: monthDays.remove(newDay)
        # remove easter
        easterSunday = easter(self.year)
        # go back two days
        _2daysLess = datetime.timedelta(days=-2)
        goodFriday = easterSunday + _2daysLess
        easterMonday = easterSunday + self._1daymore
        easterDays.append(datetime.datetime.strptime(str(goodFriday),'%Y-%m-%d' ).strftime('%Y%m%d'))
        easterDays.append(datetime.datetime.strptime(str(easterMonday),'%Y-%m-%d' ).strftime('%Y%m%d'))
        for easterDay in easterDays:
            if easterDay in monthDays: monthDays.remove(easterDay)

        return monthDays







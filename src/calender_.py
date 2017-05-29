import calendar
import datetime

class Calender:
    def __init__(self):
        calendar.setfirstweekday(calendar.MONDAY)
        self.calendar = calendar.Calendar()
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
        return tradingDays

    # removes the weekends from the days of the month
    def isWeekday(self,date):
        day = calendar.weekday(int(date[0:4]),int(date[4:6]),int(date[6:8]))
        if day < 5:
            return True
        else:
            return False

    #removes a monday from the list if the holiday is on a Sunday
    def isHolidayOnSunday(self,day):
        date = datetime.datetime.strptime(str(day), '%Y%m%d').strftime('%Y-%m-%d')
        splitDate = date.split('-')
        whichDay = calendar.weekday(int(splitDate[0]), int(splitDate[1]), int(splitDate[2]))
        if whichDay == 6: #if Sunday
            #if the day is a single digit i.e 1,2,3, add new date then fill with a leading zero
            if(len(str(int(splitDate[2]))) == 1):
                newHoliday = int(splitDate[2]) + 1
                newHoliday = str(newHoliday).zfill(2)
            # if the day is a double digit i.e 12,21,30 , add new date only
            else:
                newHoliday = int(splitDate[2]) + 1
            holidayDate = splitDate[0]+self._strMonth+str(newHoliday)
            return holidayDate
        return day

    # removes the holidays from the days of the month
    def holiday(self,monthDays):
        if self.month in self.publicHolidays.keys():
            days = self.publicHolidays.__getitem__(self.month)
            for day in days:
                newDate = str(self.year) + str(self.month) + day
                newDay = self.isHolidayOnSunday(newDate)
                if newDay in monthDays: monthDays.remove(newDay)
        return monthDays

        #Good Friday
        #Easter Monday
        #Idd – ul - Fitr
        # Eid al Adha --- as of sep 2016










import calendar
import datetime

class Calender:
    def __init__(self):
        calendar.setfirstweekday(calendar.MONDAY)
        self.calendar = calendar.Calendar()

    def getDayInMonth(self,year,month):
        weekdays = list()
        for date in self.calendar.itermonthdates(year,month):
            newDate = datetime.datetime.strptime(str(date), '%Y-%m-%d').strftime('%Y%m%d')
            weekday = self.isWeekday(newDate)
            if weekday:
                if int(newDate[4:6]) == month:
                    weekdays.append(newDate)
        return weekdays

    def isWeekday(self,date):
        day = calendar.weekday(int(date[0:4]),int(date[4:6]),int(date[6:8]))
        if day < 5:
            return True
        else:
            return False

    def holiday(self):
        pass
        #New Year's Day 1st January
        #Good Friday
        #Easter Monday
        #Labour Day 1st May
        #Madaraka Day* 1st June
        #Idd – ul - Fitr
        # Eid al Adha --- as of sep 2016
        #Mashujaa Day* 20th October
        #Jamhuri (Independence) Day* 12th December
        #Christmas Day 25th December
        #Boxing Day 26th December






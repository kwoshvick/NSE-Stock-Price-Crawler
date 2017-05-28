import calendar
import datetime

class Calender:
    def __init__(self):
        calendar.setfirstweekday(calendar.MONDAY)
        self.calendar = calendar.Calendar()

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
        return weekdays

    # removes the weekends from the days of the month
    def isWeekday(self,date):
        day = calendar.weekday(int(date[0:4]),int(date[4:6]),int(date[6:8]))
        if day < 5:
            return True
        else:
            return False

    # removes the holidays from the days of the month
    def holiday(self,days):
        # New Year's Day 1st January
        if self.month == 1:
            day = str(self.year)+str(self.month)+'01'
            if day in days: days.remove(day)
        # Labour Day 1st May
        elif(month == 5):
            day = str(self.year) + str(self.month) + '01'
            if day in days: days.remove(day)
        # Madaraka Day* 1st June
        elif(month == 6):
            day = str(self.year) + str(self.month) + '01'
            if day in days: days.remove(day)
        # Mashujaa Day* 20th October
        elif (month == 10):
            day = str(self.year) + str(self.month) + '20'
            if day in days: days.remove(day)
        # Jamhuri (Independence) Day* 12th December
        elif (month == 5):
            day = str(self.year) + str(self.month) + '12'
            if day in days: days.remove(day)
        # Christmas Day 25th December
        elif (month == 5):
            day = str(self.year) + str(self.month) + '25'
            if day in days: days.remove(day)
        # Boxing Day 26th December
        elif (month == 5):
            month.pop()


        pass

        #Good Friday
        #Easter Monday
        #Idd – ul - Fitr
        # Eid al Adha --- as of sep 2016










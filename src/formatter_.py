import os
import csv

class FormatData:
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

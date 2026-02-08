# Count the number of instances of a particular weekday in a given month/year

# You're given a month and a year, along with a day of the week (Monday through Sunday).
# Your task: Return the number of instances of that day of the week in the given month.

# Parameters
# year: Four-digit year
# month: Two-digit month
# whichday: Number of the weekday (0 is Monday, 6 is Sunday)

# Result
# [int: The number of times the given weekday occurs within the specified month

# Constraints
# • The year and month values are always valid calendar values.
# • The whichday argument is always 0 through 6, inclusive.

# Example 1:
# Input: 2025, 12, 0 (December 2025, Monday)
# Result: 5 (There are five Mondays in December 2025.)

# Example 2:
# Input: 2030, 1, 5 (January 2030, Saturday)
# Result: 4 (There are four Saturdays in January 2030.)

# Want a hint?
# Take a look at the calendar class in the Python documentation. The monthcalendar class will be useful.

import calendar

def count_days(year, month, whichday):
  daycount = 0
  weeklist = calendar.monthcalendar(year, month)  #monthcalendar returns an array of the weeks in a month

  for week in weeklist:
    if week[whichday] !=0:
      daycount += 1

  return daycount


daynum = count_days(2025, 12, 0)
print(daynum)
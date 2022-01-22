# 19: You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

import datetime
print(datetime.datetime(1900, 1, 1).strftime("%A"))

def get_sundays_at_20th_century():
  sundays = 0
  for year in range(1901, 2001):
    for month in range(1, 13):
      date = datetime.datetime(year, month, 1)
      if(date.strftime("%A") == 'Sunday'):
        sundays += 1
  return sundays

print(get_sundays_at_20th_century()) #171

# Correct
 
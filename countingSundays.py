# -*- coding: utf-8 -*-
'''
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''
import calendar
#returns weekday of given date
dayy=lambda x,y,z:calendar.weekday(x,y,z)==6

def nextMonth(year,month):
    '''
    returns next month of given month and year
    '''
    if(month<12):
        month=month+1
    else:
        month=1
        year=year+1
    return year,month;
    
count=0
year=1901
month=1
while year<2001:
    '''
    counts the number of sundays in first of month in the given period
    '''
    year,month=nextMonth(year,month)
    if dayy(year,month,1):
        count=count+1
        
print(count)
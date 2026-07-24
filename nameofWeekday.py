"""
Write a program to print the name of the weekday of a given date.

The date in string format is like "8 Feb 2021".
"""
import datetime 
date_str = input("Enter date in format 'DD MMM YYYY': ")
date_obj = datetime.datetime.strptime(date_str, "%d %b %Y")
date_day = date_obj.strftime("%A")
print(date_day)
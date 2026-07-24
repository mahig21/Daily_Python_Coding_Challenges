"""
You are given a date D1 and an integer Y.
Write a program to add the years Y to D1 and display the new date D2.
Note: Assume 1 year has 365 days
"""
import datetime
date_str=input()
years=int(input())
current_date=datetime.datetime.strptime(date_str,"%b %d %Y")
delta=datetime.timedelta(days=365*years)
new_date=current_date+delta 
print(new_date)

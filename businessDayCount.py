#24-02-26
"""
Given a start date and an end date, return the number of business days
between the two.

- Given dates are in the format "YYYY-MM-DD".
- Weekdays are business days (Monday through Friday).
- Weekends are not business days (Saturday and Sunday).
- Include both the start and end dates when counting.
"""
import datetime
def count_business_days(start, end):
    weekdays=0
    startDate=datetime.datetime.strptime(start,"%Y-%m-%d")
    endDate=datetime.datetime.strptime(end,"%Y-%m-%d")
    delta=datetime.timedelta(days=1)
    while(startDate!=endDate):
        day=startDate.strftime("%A")
        if day!="Sunday" and day!="Saturday":
            weekdays+=1
        startDate=startDate+delta
    day=endDate.strftime("%A")
    day=startDate.strftime("%A")
    if day!="Sunday" and day!="Saturday":
        weekdays+=1
    return weekdays
weekdays=count_business_days("2026-02-24", "2026-02-28")
print(weekdays)

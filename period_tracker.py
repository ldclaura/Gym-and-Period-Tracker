import datetime
from calendar import monthrange
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
def next_period(start_day, *average):
    """Returns date and month of next period In Tuple (date, month) If average not specified defaults to 28"""
    current_month = datetime.datetime.now().month
    current_year = datetime.datetime.now().year
    monthrange_today = monthrange(current_year, current_month)
    if average == ():
        average = (28,)
    for avg in average:
        next_p = start_day + avg
        next_p_month = current_month
        if next_p >= monthrange_today[1]:
            next_p = next_p - monthrange_today[1]
            next_p_month = next_p_month + 1
        return next_p, next_p_month
def average_mens_length(*length):
    average = round(sum(length)/len(length))
    return average
def length(date_start, month_start, year_start, date_start_2, month_end_2, year_end_2):
    current_month = datetime.datetime.now().month
    current_year = datetime.datetime.now().year
    monthrange_today = monthrange(year_start, month_start)

    leng = date_start + date_start_2 - 1
    if monthrange_today[1] <= leng - 1:
        dicks = monthrange_today[1] + (monthrange_today[1] - leng) * -1

    return monthrange_today[1], dicks
#first day of p, day before next p
#42
#40
#49
print(next_period(10,44)) #28
print(average_mens_length(42,40))#49
print(length(29, 6, 2025, 10, 8, 2025))
#id | date_start | month_start | year_start | date_end | month_end | year_end | difference
#1  | 29         | 6           | 2025       | 6        | 7         | 2025     |
#2  | 10         | 8           | 2025       | 17        | 8        | 2025     |
    #29
    #10
    #first day of p, day before next p
    #42!!!
#how much of the calculation needs to be python and how much can be sql
#should i use the func that i already made?

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
#first day of p, day before next p
#42
#40
#49
print(next_period(10,44)) #28
print(average_mens_length(42,40,49))

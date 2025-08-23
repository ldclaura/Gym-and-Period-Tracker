import datetime
from calendar import monthrange

def next_period():
    current_month = datetime.datetime.now().month
    current_year = datetime.datetime.now().year
    monthrange_today = monthrange(current_year, current_month)
    days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    print(monthrange_today[0])
    print(days[monthrange_today[0]])
    next_p = datetime.datetime.now().day + 28
    next_p_month = current_month
    if next_p >= monthrange_today[1]:
        next_p = next_p - monthrange_today[1]
        next_p_month = next_p_month + 1
    print(next_p)
    print(next_p_month)
    print(monthrange_today[1])
    print(datetime.datetime.now().month)

next_period()
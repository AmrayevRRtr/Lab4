ex1
from datetime import datetime, timedelta
def subtract_5_days(x):
    current_date = datetime.now()
    sub_date = current_date - timedelta(x)
    return str(sub_date)
print(subtract_5_days(5))
ex2
from datetime import datetime, timedelta
now = datetime.now()
x = 1

def yesterday():
    yesterdayy = now - timedelta(x)
    print(yesterdayy.strftime("%A"), ",", yesterdayy.strftime("%d"), "of", yesterdayy.strftime("%B"))

def tomorrow():
    tomorroww = now + timedelta(x)
    print(tomorroww.strftime("%A"), ",", tomorroww.strftime("%d"), "of", tomorroww.strftime("%B"))

yesterday()
print(now.strftime("%A"), ",", now.strftime("%d"), "of", now.strftime("%B"))
tomorrow()
ex3
from datetime import datetime

def drop_microseconds(dt):
    return dt.replace(microsecond=0)

current_datetime = datetime.now()
datetime_without_microseconds = drop_microseconds(current_datetime)
print("Original datetime:", current_datetime)
print("Datetime without microseconds:", datetime_without_microseconds)
ex4
from datetime import datetime

def date_diff_in_sec(date1, date2):
    timediff = abs(date2 - date1)
    return timediff.total_seconds()
date1 = datetime(2023, 1, 1, 10, 5, 5)  
date2 = datetime(2023, 1, 1, 12, 0, 0) 
difference_seconds = date_diff_in_sec(date1, date2)
print("Difference in seconds:", difference_seconds)
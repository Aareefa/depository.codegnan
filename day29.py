'''
Datetime Method
---------------
->To work with date and time will use this datetime

import datetime
today = datetime.date.today()
print(today)

import datetime
now = datetime.datetime.now()
print(now.time())

Common format code
------------------
%d ---- Day
%m ----- Month
%Y ------ Year
%H ------- Hours
%M ----- Min
%S ----- Sec

strftime()
---------
->This used to format date and time

import datetime
now = datetime.datetime.now()
print(now.strftime("%d-%m-%Y"))
print(now.strftime("%H:%M:%S"))

import datetime
Day_1 = datetime.date(2026,1,26)
Day_2 = datetime.date(2026,2,26)
Diff =Day_1 - Day_2
print(Diff.days)
'''
import datetime
any=datetime.datetime.now()
print(any.hour)
print(any.minute)
print(any.second)
print(any.microsecond)







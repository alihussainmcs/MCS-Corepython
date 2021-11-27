"""
#  date time is very important in daily life for calculating bank interests, fds, project delivery dates everything
# depends on three modules in python are :
1. datetime,
2.time,
3.calendar

epoch is the point where tie starts,   epoch is used time function in time module

"""

# using epoch

import time

epoch = time.time()
print("current time :", epoch)

dt = time.localtime()
print(dt)

# retrieve  date time using epoch


import time
x = time.localtime(1632571540.8761873)

# for date
d = x.tm_mday
m = x.tm_mon
y = x.tm_year
print("current date: %d - %d - %d" % (d, m, y))

# for time
h = x.tm_hour
m = x.tm_min
s = x.tm_sec
print("current time : %d : %d : %d" % (h, m, s))


# 3. convert epoch into current time using ctime function

t = time.ctime(1632571540.8761873)
print(t)

# ctime()-function of time module,
# now()-method of datetime module,
# today() method of datetime

# 4. to know current date and time
import time
t = time.ctime()
print(t)

# 5.to know the local date time

from datetime import *
now = datetime.now()
print(now)

print("current date : {} / {} / {}" .format(now.day, now.month, now.year))
print("current time : {} : {} : {}".format(now.hour, now.month, now.second))

print("6. To know today's date and time")

from datetime import *

# today() class gives date and time
tdm = datetime.today()
print("Today's day and time: ", tdm)

# today() class gives date only
d = date.today()
print("Today's date :", d)

print("7. To combining date and time ")
d = date(2016, 5, 29)
t = time(17, 11, 26)
dt = datetime.combine(d, t)
print(dt)

x = date(2021, 11, 29)
y = time(22, 9, 12)
dt = datetime.combine(x, y)
print(dt)
dt1 = datetime.now()
print(dt1)

dt2 = datetime.combine(d, t)
print(dt2)

dt3 = datetime(year=1995, month=4, day=19)
print("my date of birth :", dt3)

dt4 = datetime(1995, 4, 19, 18, 30)
print(dt4)

dt5 = datetime(year=1995, month=4, day=19, hour=12, minute=22)
print(dt5)

dt6 = dt5.replace(year=1999, month=5, day=22, hour=22, minute=25, second=36)
print(dt6)

print("8. To create a date time object and then change its contents")
from datetime import *

dt1 = datetime(year=2011, month=5, day=26, hour=23, minute=36, second=15)
print(dt1)
dt2 = dt1.replace(year=2001, month=9, hour=5)
print(dt2)
print("FORMATTING dates and times: strftime()=string format time")
from datetime import *

td = datetime.today()
print(td)
print(td.strftime("%d, %B, %Y"))


print("9.To convert a date into required string format")

from datetime import *

td1 = date.today()
print(td1)
# to convert into string format
td2 = td1.strftime("%d, %B, %Y")
print(td2)
print(td.strftime("%j"))
print(td.strftime("%A"))

print("10.To find the day of the year and weekday_name")
from datetime import *

td = date.today()
print(td)
s1 = td.strftime("%j")
print("Today is the the ", s1, "th day in the current year")

s2 = td.strftime("%A")
print("It is ", s2)

'''
print("11. To format the time using strftime() method")

from datetime import *

dt = datetime.now()
# print current time
print(dt)
print("current time:", dt.strftime("%H : %M : %S"))

d, m, y = {int(x) for x in input("Enter a date: ").split('/')}
dt = date(y, m, d)
print(dt.strftime("%W, %A"))

print("11.To format the time using strftime() method")

from datetime import *
dt = datetime.now()
print(dt)
print("current time : ", dt.strftime("%H : %M : %S"))

print("12. Accept date from keyboard and display the week")
from datetime import *
d, m, y = {int(x) for x in input("Enter the date:").split("/")}
dt = date(y, m, d)
print(dt.strftime('Day %W of the week. This is %A'))

print("13. To find the difference between two date")
from datetime import *

d1, m1, y1 = [int(x) for x in input("Enter the first date:").split('/')]
d2, m2, y2 = [int(x) for x in input("Enter the second date: ").split('/')]
dt = dt1 - dt2
print("days difference :", dt)
# to find difference in weeks
weeks, days = divmod(dt.days, 7)
print("weeks difference", weeks)
# to find difference in months
months, days = divmod(dt.days, 30)
print("months difference:", months)

print("difference between two point of time")
d2 = datetime(1995, 4, 19, 12, 2, 56)
d1 = datetime(2021, 9, 25, 12, 57, 16)

diff = d1 - d2

print("difference in %d days, %d seconds, %d microseconds" % (diff.days, diff.seconds, diff.microseconds))

print("14. difference between two times ")
from datetime import *

d1 = datetime(1995, 4, 19, 12, 6, 5)
d2 = datetime(2021, 6, 12, 11, 5, 6)

difference = d2 - d1
# divide days by 7 returns number of weeks and remaining days
weeks, days = divmod(difference.days, 7)
# divide seconds by 3600 returns number of hours and remaining seconds
hrs, secs = divmod(difference.seconds, 3600)
min = secs//60
secs = secs % 60
print("difference in %d weeks, %d days, %d hrs, %d min, %d secs" %(weeks, days, hrs, min, secs))

print("16.To find future date and time from an existing date and time ")
from datetime import *
d1 = datetime(2021, 9, 26, 16, 45, 45)
period1 = timedelta( days=15, seconds=25, minutes=12, hours=11)
print("New date and time:", d1 + period1)

print("17. To display next 10 days date time continuously")
from datetime import *
d = datetime.today()
print(d)

for x in range(10):
    nextdate = d + timedelta(days=x)
    print(nextdate)

print("comparing two dates: d1 == d2, d1 > d2, d1 < d2")
print("18. To accept date of births of two persons determining the older person")

d1, m1, y1 = [int(x) for x in input("enter date of birth (dd/mm/yyyy):").split('/')]
b1 = date(y1, m1, d1)
d2, m2, y2 = [int(x) for x in input("enter date of birth (dd/mm/yyyy):").split('/')]
b2 = date(y2, m2, d2)

if b1 == b2:
    print("Two persons are same age")
elif b1 < b2:
    print("The first person is older")
else:
    print("The second person is older")

print("19. sort a group of dates in ascending order")
from datetime import *

group = []
group.append(date.today())
d = date(2021, 6, 8)
group.append(d)
d = date(2012, 5, 8)
group.append(d)

group.append(d + timedelta(days=25))
group.sort()

for d in group:
    print(d)
print("example 2")
list = []
list.append(date.today())
d = date(2012, 6, 6)
list.append(d)
d = date(2011, 5, 8)
list.append(d)

list.append(d+timedelta(days=30))

list.sort()

for d in list:
    print(d)

print("19.print random in range with some delay between each other")

import time, random

for i in range(10):
    num = random.randrange(100, 200, 10)
    print(num)
# time.sleep(1.5)

print("20. To find execution of program")


# Python program to show time by perf_counter()
from time import perf_counter
from time import sleep

t1 = perf_counter()
i, sum = 0, 0
while(i < 100000):
    sum += i
    i += 1

sleep(3)

t2 = perf_counter()
print("Execution time = %f seconds" % (t2-t1))

print("21. to find leap year")

from calendar import *

y = int(input("Enter year: "))
if(isleap(y)):
    print(y, 'is a leap year')
else:
    print(y, "is not a leap year")

from calendar import *
print(month(2016, 5))

print("22. to display calendar of given year and month")

yy = int(input("enter year: "))
mm = int(input("enter month: "))

str = month(yy, mm)
print(str)

print("23.print entire calendar")

from calendar import *

y = int(input("enter the year: "))
print(calendar(y, w=3, l=1, c=6, m=3))
'''

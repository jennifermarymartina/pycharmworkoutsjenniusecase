from datetime import datetime, date, time

s="Inceptez"

print("Length of Inceptez:", len(s))


now =datetime.now()
print(now)

today = date.today()
print(today)

#Create specific date or time
d=date(2020, 12, 31)
t=time(10,10,10)
dt=datetime(2020, 12, 31, 10, 10, 45)

print(d)
print(t)
print(dt)

from datetime import timedelta

today=datetime.today()
tomorrow=today + timedelta(days=1)
yesterday=today - timedelta(days=1)
next_week=today + timedelta(days=7)
next_month=today + timedelta(days=30)
plus_5_days = today + timedelta(days=5)
minus_2_hours = today - timedelta(hours=5)

print("====================")
print(today)
print(tomorrow)
print(next_week)
print(next_month)
print(plus_5_days)
print(minus_2_hours)


#Date difference

#d1-d2
#Format datetime using strftime - to convert datetime from one format to another

dt1=now.strftime("%Y-%m-%d %H:%M:%S")
print(dt1)

dt1=now.strftime("%m/%d/%Y %H:%M:%S")
print(dt1)

dt1=now.strftime("%d/%m/%Y %H:%M:%S")
print(dt1)

#Parse string to datetime
dt1=datetime.strptime('2020-12-31','%Y-%m-%d')
print(dt1)
strdate="05/06/2025"
#output= 2025-06-05

dtf1=datetime.strptime(strdate,"%d/%m/%Y")

print(dtf1)
strf1=dtf1.strftime("%Y-%m-%d")
print(strf1)
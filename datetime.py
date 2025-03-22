# import the date time module
from datetime import datetime

#To get the current date and time
a= datetime.datetime.now()

#the current datetime stored in var a
# to get current date time
print(a)

#to extract  year using lambda
year = lambda x:x.year

#To extract month
month = lambda x:x.month

# to extract date
date = lamda x:x.date

# to extract time
time = lamda x:x.time

#print the output
print(year(a))
print(month(a))
print(date(a))
print(time(a))
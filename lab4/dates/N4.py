import datetime
a = datetime.datetime(2018, 7, 27)
b = datetime.datetime(2011, 4, 21)

c = a - b
print(c.days*24*60*60)
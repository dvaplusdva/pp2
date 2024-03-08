import datetime

x = datetime.datetime.now()
y = x - datetime.timedelta(days=1)
t = x + datetime.timedelta(days=1)
print(y, ";", x, ";", t)

import datetime

x = datetime.datetime.now()

b = x.replace(microsecond=0)

print(b)



import datetime as dt

fmt = '%a %d %b %Y %H:%M:%S %z'

n = int(input())

for _ in range(n):
    d1 = dt.datetime.strptime(input(), fmt)
    d2 = dt.datetime.strptime(input(), fmt)
    print(int(abs((d1-d2).total_seconds())))

from datetime import date
import calendar
import string

m,d,y = map(int, input().split())

my_date = date(y, m, d)

print(calendar.day_name[my_date.weekday()].upper())


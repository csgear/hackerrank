import re

exp = "^[+-]?[0-9]*\.[0-9]+$"

m = int(input())

for _ in range(m):
    s = input()
    print(bool(re.match(exp, s)))
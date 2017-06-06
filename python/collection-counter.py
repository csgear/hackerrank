from collections import Counter

n = int(input().strip())

shoes = Counter(map(int, input().strip().split()))

m = int(input().strip())

income = 0

for i in range(m):
    size, price = map(int, input().strip().split())
    if shoes[size] != 0:
        income += price
        shoes[size] -= 1

print(income)


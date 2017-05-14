n, l = int(input()), list(map(int, input().split()))

print(all(item > 0 for item in l) and any(n < 10 or n % 11 == 0 for n in l))
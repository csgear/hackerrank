m = int(input().strip())
s1 = set(map(int, input().strip().split()))
n = int(input().strip())
s2 = set(map(int, input().strip().split()))

s = s1.symmetric_difference(s2)

print(*sorted(s), sep='\n')

### hackranker.com

n = input()
s1 = set(input().split())

m = int(input())

for i in range(m):
    eval('s1.{0}({1})'.format(input().split()[0], input().split()))

print(sum(map(int, s1)))
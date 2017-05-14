
m,n = map(int, input().split())

data = list()

for _ in range(m):
    data.append(list(map(int, input().split())))

k = int(input())

def getkey(item):
    return item[k]

s = sorted(data, key=getkey)

for i in range(len(s)):
    print(*s[i], sep=' ')
#   print(' '.join(map(str, s[i])))


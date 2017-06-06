s = set(input().split())

answer = True

for _ in range(int(input())):
    if (s.issuperset((input().split())) == False):
        answer = False
        break

print(answer)
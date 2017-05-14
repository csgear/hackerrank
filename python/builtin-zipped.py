
m,n = map(int, input().split())

data = list()

for _ in range(n):
    data.append(map(float, input().split()))

score = list(zip(*data))

for i in range(len(score)):
    print(sum(score[i]) / len(score[i]))

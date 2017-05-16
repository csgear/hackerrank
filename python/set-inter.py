s1, s2 = [set(input().split()) for _ in range(4)][1::2]

print(len(s1.intersection(s2)))
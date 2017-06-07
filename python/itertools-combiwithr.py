## hackranker.com itertools combinations_with_replacement

from itertools import combinations_with_replacement

s, n = input().split()

for j in combinations_with_replacement(sorted(s), int(n)):
    print(''.join(j))

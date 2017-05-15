
import itertools as iter

k, m = [int(x) for x in input().split()]

arr = []

for _ in range(k):
    arr.append(list(map(int, input().split()))[1:])

all_combination = list(iter.product(*arr))

def func(nums):
    return sum( x * x for x in nums) % m

print(max(list(map(func, all_combination))))




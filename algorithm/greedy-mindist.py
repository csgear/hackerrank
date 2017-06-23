#!/bin/python3

### hackerrank.com Minimum Absolute Difference in an Array

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# your code goes here
a = sorted(a)

res = 1e10

for i in range(1, len(a)):
    if (a[i] - a[i - 1] < res):
        res = a[i] - a[i - 1]

print(res)

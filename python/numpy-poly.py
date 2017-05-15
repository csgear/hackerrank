import numpy

poly = tuple(map(float, input().split()))

x = float(input())

print( numpy.polyval(poly, x))

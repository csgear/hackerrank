n = int(input())

s = set(map(int, input().split()))

for _ in range(int(input())):
    opt = input().split()
    if 'pop' == opt[0]:
        s.pop()
    elif 'remove' == opt[0]:
        s.remove(int(opt[1]))
    elif 'discard' == opt[0]:
        s.discard(int(opt[1]))
print(sum(s))



# another solution

#n = int(input())
#s = set(map(int, input().split()))
#for i in range(int(input())):
#    eval('s.{0}({1})'.format(*input().split()+['']))

# print(sum(s))
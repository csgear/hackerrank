
def rotate(li, x):
  return li[-x % len(li):] + li[:-x % len(li)]

def lrotate(li, x):
    return li[x % len(li):] + li[:x % len(li)]

n, d = map(int, input().strip().split())
l = list(map(int, input().strip().split()))

print(* lrotate(l, d))




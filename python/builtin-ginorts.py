
from string import ascii_lowercase, ascii_uppercase

def key(item):
    sortkey = ascii_lowercase + ascii_uppercase + "1357902468"
    return sortkey.index(item)

s = input()

print(*sorted(s, key=key), sep='')

### hackranker.com python challenge: errors and exceptions

import re

for _ in range(int(input())):
    s = input().strip()
    try:
        r = re.compile(s)
        print(True)
    except re.error:
        print(False)
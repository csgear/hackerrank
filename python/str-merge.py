
def merge_the_tools(string, k):
    for i in range(len(string) // k):
        s = string[i * k: (i + 1) * k]
        print(''.join(x for i, x in enumerate(s) if s.index(x) >= i))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
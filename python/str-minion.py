def minion_game(string):
    # your code goes here
    n = len(string)
    s = 0
    k = 0

    for i in range(n):
        if (string[i] in ('A', 'E', 'I', 'O', 'U')):
            k = k + n - i
        else:
            s = s + n - i

    if (k == s):
        print("Draw")
    elif (k > s):
        print("Kevin", k)
    else:
        print("Stuart", s)


if __name__ == '__main__':
    s = input()
    minion_game(s)
n = int(input())
for i in range(n):
    try:
        a,b = map(int, input().split())
        print(a // b)
    except ZeroDivisionError as e:
        print("Error Code: {}".format(e))
    except ValueError as e:
        print("Error Code: {}".format(e))
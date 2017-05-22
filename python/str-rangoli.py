import string

def print_rangoli(size):
    alp=string.ascii_lowercase
    for i in range(size-1,-size,-1):
        temp = '-'.join(alp[size-1:abs(i):-1]+alp[abs(i):size])
        return temp.center(4*size-3,'-')

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
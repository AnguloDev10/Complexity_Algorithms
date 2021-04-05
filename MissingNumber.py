
n = int(input())
m = input()

def missing(n,m):
    if(n < 0):
        print('We couldn´t try with a a really number')
        return 1
    else:
        if str(n) in m :
            missing(n-1,m)
        else:
            print(n)
            return 1

missing(n,m)


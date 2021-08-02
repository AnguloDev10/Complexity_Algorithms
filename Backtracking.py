n = int(input())

def weird(n):
    
    if n == 1:
        print(int(n))
        return 1 
    if n%2 == 0:
       print(int(n))
       n = n/2
       weird(n)
       
    else:
        print(int(n))
        n = n*3 + 1
        weird(n)

weird(n)
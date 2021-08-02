#First-paper
import random as ra

#a = []
#def generar(n):
#b = []
#for x in range(n):
#a.append(int(ra.randint(10,100)))



#generar(8)
#print(a)
#number2
def mostrar(lista):
    for x in lista:
        if x in lista:
            print(x)

mostrar([1,2,3,4,5])

#def reversa(lista):
results = []
a = 0
def stringmatching(p,t):
    l = len(p)
    n = len(t)
    for i in range(n-1):
        if p in t:
            results.append(p)
            a+1
        return results

stringmatching("rac", "abracadabracalamazoo")
print(results)
print(a)
#Backtracking
n = input('Please, enter a number')
print('the number is '+ n)

def weird(n):
    if(n <0):
        return []
    if(n//2 == 0):
       n = n*2
       weird(n)
    elif(n % 2 != 0):
        n = n*3 + 1
        weird(n)





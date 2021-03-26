#First-paper
import random as ra

a = []
def generar(n):
    b = []
    for x in range(n):
        a.append(int(ra.randint(10,100)))



generar(8)
print(a)
#number2
def mostrar(lista):
    for x in lista:
        if x in lista:
            print(x)

mostrar([1,2,3,4,5])

#def reversa(lista):





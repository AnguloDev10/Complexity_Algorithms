#First-paper
import random as ra

a = []
def generar(n):
    b = []
    for x in range(n):
        a.append(int(ra.randint(10,100)))



generar(8)
print(a)

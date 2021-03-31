##Python Tuples
thistuple = ("apple", "banana","cherry")
print(thistuple[-1])

#Rnage of index
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon")
print(thistuple[2:4])

#as well as the lists we hace a range of Negative indexes
##SETS
thisset = {"apple", "banana", "cherry"}
tropical={"rata","gato","cherry"}

thisset.update(tropical)
print((thisset))
#pop,discar()
thisset.pop()
#keep duplicates
thisset = {"apple", "banana", "cherry"}
tropical={"rata","gato","cherry"}
thisset.intersection_update(tropical)
print(thisset)
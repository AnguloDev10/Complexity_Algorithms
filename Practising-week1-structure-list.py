#Module2
#the main purpose for this article is practising this awesome language
##List
#are indexing,it means that the itemshave defined order
thislist = ["bad bunny","dyankee"]
print(thislist)
#Print the number of items in the list
#with function len()
#accessing data into the list
thislist = ["apple","banana","cherry"]
print(thislist[:2])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-7:-5])
#Checking if a string is into a string list
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
if "banana" in thislist:
    print("Yes, \"banana\" is there ")

#Change Item Value
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thislist[1:4]=["apple", "banana", "cherry"]
print(thislist)
print(len(thislist))
thislist =["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thislist.insert(7,"watermelon")
print(thislist)
#append
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thislist.append("red")
print(thislist)
#extend method for append  list to list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#you can add any iterable object
thislist = ["apple", "banana", "cherry"]
tropical = ("yellow","blue")
thislist.extend(tropical)
print(thislist)
#remove
thislist = ["apple", "banana","cherry"]
thislist.remove("banana")
print(thislist)
#pop
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.pop(2)
print(thislist)
#del
del tropical[1]
print(tropical)
#del and clean can hava a treatment with the list
del tropical
thislist.clear()
print(thislist)
##loop lists
#for
thislist = ["apple", "banana", "cherry"]
tropical = ["red", "yellow", "blue"]
for x in thislist:
    print(x)

for i in  range(len(tropical)):
    print(tropical[i])

#using while
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
i = 0
while i< len(tropical):
    print(tropical[i])
    i = i+1
#loop compressing the list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
[print(x) for  x in thislist]

newlist = []
for x in tropical:
    if "n" in x:
        newlist.append(x)
print(newlist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
newlist = [x for x in tropical if "n" in x]
print(newlist)
#sorting list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.sort()
print(thislist)
#reverse sorting list
tropical.sort(reverse=True)
print(tropical)
#customize sort function
def myfunc(n):
    return abs(n-50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
##Joining
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)

print(list1)
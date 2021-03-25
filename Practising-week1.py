#FucckingIdentation
def a():
 if 5 > 2 :
    print("Five is greater than two!")
 if 4 > 1 :
     print("Four is grater than two!")

a()
#Variables
#function type() for getting the type
x = 5
print(type(x))
#string
#We can declared String either by using single or double quotes
y = "jhon"
#is the same
r = 'Jhon'

#overwrite
#var a is different with A

#variablesNames
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#multiple variables
x,y,z = "Orange","Banana","Cherry"
print(x);
print(y);
print(z);
#Unpacking collections
players = ["cristiano","Messi","Cherry"]
a,b,c = players
print(a);
print(b);
print(c);
#Outputting variables
x = "awesome"
print("Python is "+ x)
x = "Python is "
y = "awesome"
z = x + y
print(z)
#Global variables
x = "awesome"
def myfunc():
    print("Python is "+ x)
myfunc()
# inside a function
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

##Built-in Data Types
#Text Type: str
#Numeric Types: int, float, complex
#Sequeenca Types: list, tuple, range
#Mapping Type: dict
#Set Types: set, frozenset
#Boolean Type: bool
#Binary Types: bytes, bytearray, memoryview

##Random
import  random
print(random.randrange(1,100))

#String are Arrays
a = "Hello, World"
print(a[1])

for x in "banana":
    print(x)

a = "Hello, World"
print(len(a))

txt = "William is handsome"
print("handsome" in txt)

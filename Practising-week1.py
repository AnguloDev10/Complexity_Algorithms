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
##checking strings
txt = "William is handsome"
print("handsome" in txt)
#if not
txt = "William is handsome"
print("handsome" not in txt)
##Slicing strings
#with a range
b = "William is the best "
print(b[3:5])
#since the start
b = "QUE ONDA PA"
print(b[:4])
#to the end
b="String is so hard"
print(b[2:])
#negative indexing
b = "Hello, world!"
print(b[-3:-1])
##Modifying strings
#upper
a = "William wapo"
print(a.upper())
#lower
a = "GAYS"
print(a.lower())
#strip
#removes spaces from the beginning and also the end
a = " Hello, GAY "
print(a.strip())
#replace
a = "Hola gente de wsp"
print(a.replace("H","w"))
#split a comom function
a = "Take away bro"
print(a.split("y"))
#we have to indicate the separation

##String Concatenation
##examples
a = "Hello"
b = "World"
c = a + b
print(c)
##adding space
a = "Hello"
b = "World"
c = a + " " + b
print(c)
#formating strings
age= 19
txt = "My name is William, I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
#Escape characters
#\'	Single Quote
#\\	Backslash
#\n	New Line
#\r	Carriage Return
#\t	Tab
#\b	Backspace
#\f	Form Feed
#\ooo	Octal value
#\xhh	Hex value

##Booleans
#bool
print(bool("Hello"))
print(bool(1))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))
#Most values are true
#any string are true except empty
#We are going to see some values are false
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

class myclass():
    def __len__(self):
       return 1
myobj = myclass()
print(bool(myobj))

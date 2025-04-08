print("Hello world")
if (5>2):
  print("betullllllllllllllllllllll") # <------ this identation -> jarak in beginning code untuk menunjukkan bagian dari block code
  #identation sangat berpengaruh pada python language -> if tidak ada identation maka code akan menghasilkan error

#variable
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#Variables do not need to be declared with any particular type, and can even change type after they have been set.

#casting
z = str(3)
w = int(3)
y = float(3)
#you want to specify the data type of a variable?? do it with casting

print(z,w,y)

#get the type of a variable
angka = 5
nama = "John"
print(type(angka))
print(type(nama))

#single and double quotes -> same(ga ngaruh)
x = "John"
# is the same as
x = 'John'

#variable names in python are case sensitive 'a' dengan 'A' berbeda

#variable names
"""
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
"""

#example, legal names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#multi words variable name
"""
Variable names with more than one word can be difficult to read.
There are several techniques you can use to make them more readable:
"""

myVariableName = "John" #camelcase
MyVariableName = "John" #pascalcase
my_variable_name = "John" #snake case

#Many Values to Multiple Variables
a, b, c = "aku", "kamu", "kita"
print(a)
print(b)
print(c)

d = e = f = "kita" #One Value to Multiple Variables
print(d,e,f)

#unpacking collection like list, tupple, etc
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#variable output
satu = "satu"
dua = "dua"
tiga = "tiga"

print(satu, dua, tiga)#<- Using a comma to separate variables will add spaces between them, while using '+' won't add any spaces


#global variable
k = 10 #<-global variable outside the function, can be used by everyone both inside or outside function
def hitung():
  print(20+k)
hitung()

"""
jika ada 2 variable dengan nama yang sama pada inside atau outside
dari function maka yang variable akan di perbarui berdasarkan value pada variable inside function
jika ingin menggunakan variable yang di inisiasi inside function menggunakan keyword global
contohhhh:
"""
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

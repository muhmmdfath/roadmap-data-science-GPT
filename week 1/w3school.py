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

#convert type
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#random Number
import random

print(random.randrange(1, 10))

#multiline strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#strings are array
a = "Hello, World!"
print(a[1])

#looping through a string
for x in "banana":
  print(x)

#string length
a = "Hello, World!"
print(len(a))

#check string
txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#check if not in string
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

# format string
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

"""
f"teks {variabel}"	Cara paling mudah dan cepat untuk gabungkan string dan data
{price:.2f}	Menampilkan angka desimal dengan 2 digit di belakang koma
{20 * 59}	Bisa langsung pakai operasi matematika di dalam {}
"""

#escape character
escape = "hello \"world\""
print(escape)

r"""
\'	Single Quote
\\	Backslash
\n	New Line
\r	Carriage Return
\t	Tab
\b	Backspace
\f	Form Feed
\ooo	Octal value
\xhh	Hex value
"""
#boolean type
print(bool("abc"))         # True
print(bool(123))           # True
print(bool(["apple"]))     # True

print(bool(False))  # False
print(bool(None))   # False
print(bool(0))      # False
print(bool(""))     # False
print(bool([]))     # False

x = 200
print(isinstance(x, int))  # True <- fungsi built-in untuk cek tipe data dalam output bool

#list items
"""
List items are ordered, changeable, and allow duplicate values.
example:
"""
thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
print(len(thislist)) #To determine how many items a list has, use the len() function:

thislist = list(("apple", "banana", "cherry"))#list constructor to make list
print(thislist)

mylist = ["apple", "banana", "cherry"]
print(type(mylist))#check data type


#change item list

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"] #<- slice dari indeks 1 sampai sebelum indeks 2
print(thislist)

#insert -> menyisipkan
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#append -> menambahkan dengan indeks terakhir
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#extend ->menggabungkan beberapa list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#extend tidak harus menggabungkan sama sama list tapi bisa juga dengan tupple, distionary, etc.
thislist = ["apple", "banana", "cherry"] # <- list
thistuple = ("kiwi", "orange") #<- tupple
thislist.extend(thistuple)
print(thislist)

#remove list
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana") #<- jika terdapat 2 item yang ditemukan dalam list maka akan menghapus item pertama
print(thislist)

#remove specified index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1) #<- jika kosong maka akan menghapus indeks terakhir
print(thislist)

#del keyword alse remove specified index
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#del keyword also can delete the list closely
thislist = ["apple", "banana", "cherry"]
del thislist

#mengosongkan isi list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#Looping Using List Comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#without list comprehesion
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#with list comprehession
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

#sintaks
#newlist = [expression for item in iterable if condition]

#contoh lain
#Filter: hanya ambil yang bukan "apple"
newlist = [x for x in fruits if x != "apple"]
#Tanpa kondisi (ambil semua)
newlist = [x for x in fruits]
#Gunakan range():
newlist = [x for x in range(10)]
#Hanya ambil angka < 5:
newlist = [x for x in range(10) if x < 5]


#Ubah Nilai (Expression)
#Ubah semua ke huruf besar:
newlist = [x.upper() for x in fruits]
#Semua jadi "hello":
newlist = ['hello' for x in fruits]
#Ganti "banana" jadi "orange":
newlist = [x if x != "banana" else "orange" for x in fruits]


#sorting
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort() #ascending default, if want to descending thislist.sort(reverse = True)
print(thislist)

#custom list
def myfunc(n):
  return abs(n - 50) #menghitung jarak(selisih n dengan 50)

thislist = [100, 50, 65, 82, 23] #100-50 = 50, 50-50 = 0, 65-50 = 15, 82-50 = 32, 23-50 = -27 (abs merubah negatif agar tetap positif)
thislist.sort(key = myfunc)
print(thislist)

# capital letters being sorted before lower case letters:

#reverse
fruits = ["apple", "banana", "cherry"]
fruits.reverse() #membalikkan urutan list yang sudah ada, tanpa mengurutkan, beda dengan sort(reverse = True)
print(fruits)

#copy list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy() #membuat list baru dengan isi list sama sebperti yang ingin di copy
print(mylist)

#atau bisa juga menggunakan list
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#use slice operator
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

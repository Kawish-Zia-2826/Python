# string = "15"
# number = 7
# string_number  = int(string)
# total  = number + string_number
# print(total)
# text  = "this is random text"
# for character in text:
#   print(character)


fruits = "  H adsfDSF fds  rry  HHHHHH"
# print(fruits[-4:-2])
text = "dsf f"

# print(fruits.upper())
# print(fruits.lower())
# print(fruits.lower())
# print(fruits.strip())
# print(fruits.rstrip("H"))
# print(fruits.replace("H"))
# print(fruits.split("H"))
# print(fruits.capitalize())
# print(len(fruits))
# print(fruits.center(50,"."))
# print(fruits.count("H"))
# print(fruits.endswith("H",1,3))
# print(fruits.endswith("H",1,3))
# print(text.isalpha())
# import time


# print( time.strftime("%H:%M:%S"))



# import time

# if int(time.strftime("%H")) >= 0 and int(time.strftime("%H")) < 12:
#     print("Good Morning")


# c  = 1
# match c:
#     case 1:
#         print("one")
#     case 2:
#         print("two")
#     case _:
#         print("default")


# for k in range(1,20,2):
#     print(k)  


# i = 0
# while i < 10:
#   print(i)
#   i += 1
# print("Hello, World!")  # prints "Hello, World!"



# i = int(input("enter a num"))
# while i == 0:
#   print("zero")
#   i = int(input("enter a num"))
# print("the loop is closed" ,i)

print("pyhton is working")
# i  =5
# while i > 0:
#   print(i)
#   i -= 1

# for i in range(12):
#     if i == 10:
#         print("its the continue loop")
#         continue
#     print(i+1)
# i  =  1
# while True:
#   print(i)
#   i += 1
#   if(100%i == 0):
#     break
# def greet(name):
#   print("Hello, " + name)
# greet("John")

# def add(a,b):
#   print(a+b)
# add(5,6)


# list = ['1',2,3,4,5,6]
# print(list[-6])  # prints 1

# list   = [ i for i in range(5)]
# print(list)


# list = [1,23,3,4,4,43534,645,656,756]
# list2 = ['a','b','c','d','e','f',str('g')]
# list.sort()
# list.sort(reverse =True)
# print(list)
# print(list.index(3))
# print(list2.count('g'))


# newlist  = list.copy()
# newlist.append("green")
# print(newlist)

# list.insert(0,'kawisj')

# list.extend(list2)

# print(list + newlist)


# tup  = (1,2,3,4,56,43,55)
# print(type(tup),tup[0:3])

# print("who is the tallest builfing in world\n")
# questions = ['burj khalifa','mnare pakistan','ambani house']
# print(questions)
# useronput = input(str('enter a name\n'))
# answer = useronput.lower()
# print(answer)
# if(answer == 'burj khalifa'):
#   print("congratulations")
# else:
#   print("wrong")
#   useronput

# letter  = "i am {1} and city is{0}"
# city ="karachi"
# name = "kawish"
# print(letter.format(name,city))

# print(f"this is f string {{5+4}}")
# def myfunc():
#   ''''this is doc '''
#   print("this is simple func")
# myfunc()

# print(myfunc.__doc__)


# def factorial(n):
#   if(n == 0 or n == 1):
#     return 1
#   return n * factorial(n-1)

# print(factorial(3))




# def recursion(n):
#   if n == 100:
#     print("stop")
#   print(n)
#   recursion(n)
# recursion(5)


# set1 = {2,3,3,5,5,5,34,34,324,32,4,32}
# set2  = {132,32,12,12,3,213,123,213,12,312,312,3,423,4,234,}
# print(set1.union(set2))
# set1.update(set2)
# print(set1)

# i = 10
# while i > 0:
#   print(i)
#   i -=  1 

# set1 = {"apple", "banana", "cherry"}
# set2 = {1, 5, 7, 9, 3}
# set3 = {True, False, False}
# set1.add("new fruit")
# set1.discard('apple')
# print(set1)

object =  {
  "name":"kawihs",
  "last":"last"
}
myfamliy = {
  "child1":{
    "name":"child 1"
  },
  "child2":{
    "name":"child 2"
  }
}
# print(object['name'])
# print(object.get('name'))

# print(object.keys())
# print(object.values())
# print(object.items())
# val = object.values()
# if "kawihs" in val:
#   print("right")
# object.update({"name":"kawish","class":"125h"})
# print(object)
# object.popitem()
# print(object)

# for x in object.items():
#   print(x)
# del object
# print(object)

# for x,y in object.items():
#   print(x,y)
# print(object.items())


# for x,y in myfamliy.items():
#   print(x,y)

#   for j in y:
#     print(y['name'])

# print("yes ")  if 1 > 0 else print("not") if 2>9 else print("nothing")


# i =  1
# while  i < 11:
#   i +=1
#   if(i==2):
#     continue
#   print(i)


# for x in range(1,10,2):
#   if x == 3:continue
#   print(x)
# for c in range(10):
#   pass


# add = lambda x,y:x +y
# print(add(4,5))


# multiply =  lambda a,b :a*b

# print(multiply(5,5))


# def greet(name ="kawish",**k):
#   print(name + " func is calling " + k['sdfsd'])
#   print(type(k))
# greet( "jawad",sdfsd="dsfds")


# def myfunc(n):
#   return lambda a : a * n



# myfuncc = myfunc(2)


# print(myfuncc(5))


# table  = input("enter a num\n")
# for i in range(1,11):
#   print(f"{table} * {i}  = {int(table) * i}")


# try:
#   name = int("k")
# except   :
#   print("wrong number" )
# print("hiu")


# def check(n):
#   try :
#     n = int(input("enter a num"))
#     return print(n)
    
#   except:
#     print("wrong num")
#     check(n)


# check(n=0)


# try:
#   k = int("a")
#   b = ['a','b','df']
#   print(b[90])
# except ValueError:
#     print("val err")
# except IndexError:
#    print("index err")
# finally:
#    print("i am always print")

# print("worling")


# num  = int(input("neter a num bw 5 or 10"))

# if num >= 5 and num <= 10:
#   raise  ValueError("num bw sdfmsdlkfhsdjkf")
# import random
# user_input = input("enter code or decode\n")
# if user_input == "code":
#   code = input("enter a code\n")
#   if len(code) >= 3:
#     char = code[0]
#     code = code[1:]  + char
#     random_char=['a','b','c','d','e','f','g','h','i','j','k','l','m','n']
#     code = (random.choice(random_char) * 3) + code + (random.choice(random_char) * 3)
#     print("the code is",code)
# elif user_input == "decode":
#   decode = input("right a decode word")
#   if len(decode) <= 3:
#     decode[::-1]
# else : print("sahi likho")

# print("a") if 3>2 else print("b")

# c  = 9  if 3> 2 else 0
# print(c)

# list = [1,2,3,2,2,3,23,213,21,32,13,21,321,3,123]
# for index, x in enumerate( list):
#   # print(x)
#   print(index)


# from math import sqrt as s 
# import math as m 

# print(m.sqrt(9))


# print(dir(m))


# from module import welcome,kawish
# from module import *


# welcome()


# import module

import os


# print(os.getcwd())

# os.mkdir("new")
# os.isfile(os.getcwd() + "\nawa")
# os.rmdir("newagain")

# x = 10
# def abc():
#   global x
#   x = 4
#   print(x)

# # abc()
# print(x)
# file  = open('text.txt','r')
# content = file.read()
# print(content)
# file.close()

# with open('text.txt','a') as file:
#   file.write("dsfdsf")


# file  = open('text.txt','w')
# with open('text.txt','a') as file :
#     file.write("thie is some text\n")




# import os 

# os.remove("text.txt")




# with open("text.txt",'a')as file:
  
# print(__name__)



#   print(file.readline())


# f = open('text.txt', 'r')
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)



# with open('text.txt','r') as file:
#   while True:
#     filee = file.readline()
#     print(filee)
#     if not filee:
#       break


# with open('text.txt','r') as f:
#   f.seek(10)
#   print(f.tell())

#   print(f.read(5))


# with open('sample.txt','w')as file:
#   file.write("this is some text")
#   file.truncate(2)



# def add(x,y):
#   print("this is add func")
#   return x+y


# def sub(x,y):

# def appl(func,y):
#   return log(func) + y
# log = lambda x: x*2 +3

# print(appl(2,2))
# def add(x,y):
#   return x *y
# l = [1,2,3,4,5,6,7,8,9,10]
# print(list(map(add,2,l)))


# from functools import reduce


# print(reduce(lambda x,y:x+y,l))

# class person:
#   name = "kawish"
#   classs  = "12th"
#   def info(self):
#     print(f"this person name is {self.name} and class is {self.classs}")


# rizwan = person()
# rizwan.name = "rizwan"
# rizwan.classs = "12th"

# rizwan.info()

# mujeeb = person()
# mujeeb.name = "mujeeb"

# mujeeb.info()


# class peson:
#   def __init__(self,name,classs):
#     print("this is init func")
#     self.name = name
#     self.classs = classs
#   def info(self):
#     print(f"this person name is {self.name} and class is {self.classs}")


# a = peson("kawihs","12th")
# a.info()

# def decorator(func):
#   def wrapper():
#     print("function call ho gya hai")
#     func(a,b)
#   return wrapper

# # @decorator
# def add(a,b):
#   print(a+b)

# add(5,5)





# def decorator(func):
#   def wrapper(a,b):
#     print("function call ho gya hai ")
#     func(a,b)
#   return wrapper



# # @decorator
# def add(a,b):
#   print("this is add func")
#   print(a+b)

# decorator(add)(5,5)


# class mycalss:
#   def __init__(self,n):
#     self.name = n
#   def showName(self):
#       print(f"the name is {self.name}")

#   @property
#   def namee(self):
#     return 5*self.name
  
#   @namee.setter
#   def namee(self,n):
#     self.name = 2*n

# p1 = mycalss(5)

# p1.namee = 5
# print(p1.namee)
# print(p1.name)

# print(p1.namee)
# p1.showName()



# class calculation:
#   def __init__(self,a,b):
#     self._a = a
#     self._b = b
#   def add(self):
#     return self._a + self._b
#   @property
#   def a(self):
#     return self._a *2 + self._b
#   # @a.setter
#   # def a(self,newval):
#     # self.a = self._a * newval + self._b
# cal1 = calculation(5,5)
# print(cal1.add())
# cal1.a  = 10
# print(cal1.a)



# class MyClass:
#   def __init__(self,v):
#     self.val = v
#   @property
#   def getVal(self):
#       return self.val
#   @getVal.setter
#   def getVal(self,v):
#      self.val  =v  





# p1 = MyClass(20)
# p1.val = 50
# print(p1.getVal)


# class Kawish:
#     def __init__(self, name):
#         self.namee = name  # Ensure consistent attribute naming

#     def showName(self):
#         print(f"This name is {self.namee}")  # Use the correct attribute

#     @property
#     def getVal(self):  
#         return self.namee  # Return the correct attribute
#     @getVal.setter
#     def getVal(self,nval):
#         self.namee = nval

# p1 = Kawish("Kawish")

# p1.getVal = "jawad khan"

# print(p1.getVal)  # Access property without parentheses


# class emp:
#   def __init__(self,n,a,i):
#     self.name = n
#     self.age = a
#     self.id = i
#   def show(self):
#     print(f"the name is {self.name} and age is {self.age} and id is {self.id}")



# class manager(emp):
#   def salary():
#     print("this is salary func")


# p1 = emp("kawish",23,1)
# p2  = manager("jawad",23,2)
# p2.show()

# p1.show()

# class p:
#   def __init__(self):
#     self._name = "kawish"
#   def _show(self):
#     print(self._name) 

# class p1(p):
#   pass

# p4 = p()
# print(p4._name)

# p2  = p1()
# p2._show()

# print(p1._p__name)


# class Library:
#   def __init__(self,booksName ):
#     self.booksNo = 0
    
#     self.booksName  =booksName
#   def showBooks(self):
#     print(f"the book no is {self.booksNo} and name is {self.booksName}")
  
    


# c1 = Library("kawish")
# c2 = Library("jawad")
# c3 = Library("asd")
# c3.showBooks()
# c1.showBooks()
# c2.showBooks()


# class Library:
#     def __init__(self):
#         self.books = 0
#         self.booksName = []
#         self.loadBooks()  # File se books load karne ke liye

#     def addBooks(self, n):
#         self.book = n
#         self.booksName.append(self.book)
        
#         # Book ko file me store karna
#         with open("books.txt", 'a') as file:
#             file.write(self.book + "\n")

#         self.books += 1
#         print(f'Book "{self.book}" added successfully!')

#     def loadBooks(self):
#         """File se books load karne ke liye"""
#         try:
#             with open("books.txt", 'r') as file:
#                 self.booksName = [line.strip() for line in file.readlines()]
#                 self.books = len(self.booksName)
#         except FileNotFoundError:
#             # Agar file nahi mili to koi masla nahi
#             self.booksName = []
#             self.books = 0

#     def showBooks(self):
#         if self.books == 0:
#             print("No books available.")
#         else:
#             print("\nBooks in Library:")
#             for book in self.booksName:
#                 print(f"- {book}")
#             print(f"\nTotal number of books: {self.books}")

# # Library object
# c1 = Library()

# # Add book
# c1.addBooks("adfs")

# # Show books
# c1.showBooks()


# class static:
#  def __init__ (self):
#   print("this is static method")
#  @staticmethod
#  def show():
#   print("this is static method")

# a = static()

# static.show()


# class car:
#   carname = "audi"
#   def __init__(self,name):
#     self.name = name
#   def show(self):
#     print(f"the car name is {self.carname} and the buyer name is {self.name}")


# b1 = car("kawish")
# b2 = car("jawad")
# b1.carname = "bmw" 
# car.carname = "new car"

# car.show(b1)  
# car.show(b2)  


# import os



# for i in range(10):
#   os.rename(f"new/{i}sadsad")


# class car:
#   carName = "audo"
#   def show(self):
#     print(f"this is init func and the emp name is {self.name} and the car name is {self.carName}")
#   @classmethod
#   def changeCar(cls,name):
#     cls.carName = name


# e1  = car()
# e1.name = "kawish"

# e1.show()

# e1.changeCar("bmw")
# print(e1.carName)

# e1.show()


# class person:
#   def __init__(self,name,age):
#     self.name = name
#     self.age = age
#   def show(self):
#     print(f"the name is {self.name} and age is {self.age}")
#   @classmethod
#   def fromStr(cls,string):
#         return cls(string.split('-')[0],string.split('-')[1])

# string =  "kawish-23"
# p1 = person.fromStr(string)
# p1.show()



# class emp:
#   def __init__(self,name,age):
#     self.name = name
#     self.age = age
  

# class prog(emp):
#   def __init__(self,name,age,progLang):
#     super().__init__(name,age)
#     self.progLang = progLang



# p1  = prog("kawish",23,"python")
# print(p1.name)  
# print(p1.age)

# # print(p1.__dict__)
# # print(p1.__dir__)

# string = "sdf"

# # print(dir(string))
# print(help(emp))


# class books:
#     def __init__(self,n):
#         self.name = n
#     def __len__(self):
#         return len(self.name)
#     def __str__(self):
#         return f"this is book auther name"
#     def __repr__(self):
#         return "this is repre mrthod "      # ✅ Calls __str__ → Output: Book Name: Kawish


# p1 = books("kawish")
# print(len(p1))  # ✅ Calls __len__ → Output: 6
# print(str(p1))  # ✅ Calls __str__ → Output: Book Name: Kawish
# print(repr(p1))  # ✅ Calls __repr__ → Output: Book Name: Kawish





# class animal:
#   def sounds(self):
#       return "this is animal sound"
  
# class sound(animal):
#    def sound(self):
#        abc = super().sounds()
#        return abc + "this is sound of animal"
   

# a1 = sound()
# print(a1.sound())
import os

# folder_path = "C:/Users/PC/Desktop/Python/Ulitimate_Python/clutterFolder"  # Windows
# # folder_path = "/home/yourname/MyFolder"  # Linux/Mac

# # for i in range(10):
# #     with open(file_path, 'w') as file:
# #         file.write("")  # Empty file create karega

# file_path = os.path.join(folder_path, f"text1.png")  # Correct way to join paths
# print(file_path)


# files =os.listdir("./clutterFolder")
# i = 0
# for file in files:
#     # print(file)
#     if file.endswith(".png"):
#         print(file)
#         os.rename(f"clutterFolder/{file}",f"clutterFolder/{i}.png")
#         i += 1


# print(files)


# class Vector:
#   def __init__(self,i,j,k):
#     self.i = i
#     self.j = j
#     self.k = k
#   def __add__(self,other):
#     return Vector(self.i + other.i, self.j + other.j, self.k + other.k)
#   def __str__(self):
#     return f"Vector({self.i},{self.j},{self.k})"



# v1 = Vector(1,2,3)
# v2 = Vector(4,5,6)  
# print(v1 + v2)





# input1 = int(input("enter a num 1"))
# input2 = int(input("enter a num 2"))

# print("Total",input1 + input2)



# squre = float(input("enter a side of squre"))
# inp1 = float(input("enter a side of squre"))
# inp2 = float(input("enter a side of squre"))

# print("the area of squre is",(inp1 + inp2)/2)


# a = "this is the a func"

# print(len(a))
# print(a.count("i"))

# inp = int(input("enter a num: "))
# if inp % 2 == 0:
#   print("even")
# else:

#   print("odd")


# a,b,c = 1,2,3
# if (a>b and a>c):
#   print("a is greater")
# elif (b>c):
#   print("b is greater")
# else:
#   print("c is greater")

# fmovie = input("enter a fav movie")
# smovie = input("enter a fav movie")
# tmovie = input("enter a fav movie")
# list = []
# list.append(fmovie)
# list.append(smovie)
# list.append(tmovie)
# print(list)


# list = [1,2,3,2,1]
# list2  = list.copy()
# list2.reverse()
# # print(list)
# # print(list2)
# if list == list2:
#   print("palindrome")
# else:
  # print("not palindrome")


# tuple = ("A","B","C","D","E","A","A")
# list  = list(tuple)
# list.sort(reverse = True)
# print(list)
# print(tuple.count("A"))


# dict ={
#   "name":"kawish",
#   "study":{
#     "subject":"math",
#     "class":"12th"

#   }
# }

# dict["name"] = "jawad"
# print(dict)


# dict={
#   "table":["a piece of furnityre","list of fact and fiure"],
#   "cat":"a small animal"
  
# }

# print(dict)
# set   = {"python","c++","java","c","pyhton","c++","java","html","css"}


# print(len(set))


# dict = {}

# dict["math"] = 50
# dict["phy"] = 50
# dict["chem"] = 50

# print(dict)



# list = {3,2,3,23,23,23,2,32,3,23,2,32,3}
# print(len(list))
# dict = {
# }
# dict.update({"chem":45,"com":32})

# print(dict)
# i  = 100000
# while i>=1:
#   print(i)
#   i-=1

n = 5
for i,x in enumerate(range(1,11)):
   i+1
   print(i*5)

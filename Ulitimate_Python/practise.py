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



with open('text.txt','r') as file:
  while True:
    filee = file.readline()
    print(filee)
    if not filee:
      break

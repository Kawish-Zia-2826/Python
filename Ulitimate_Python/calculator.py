print("hi this is simple calculator i made using python programing ")
print("enter a num 1 ")
num1 = int(input())
print("enter a num 2 ")
num2 = int(input())
print("enter a operator ")
operator = input()
if operator == "+":
  print(num1 + num2)
elif operator == "-":
  print(num1 - num2)
elif operator == "*":
  print(num1 * num2)
elif operator == "/":
  print(num1 / num2)
else:
  print("invalid operator")
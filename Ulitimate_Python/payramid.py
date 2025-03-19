print("payramid start" )
# n = int(input('enter a num\n'))
# for i in range(5):
#   print(" " *(n-i-1),end="")
#   print("*" *(2*i+1))


rows = int(input("Kitni lines ka pyramid chahiye? "))

for i in range(1,rows +1):
  print(" " *(rows - i) + "* " * i)
  




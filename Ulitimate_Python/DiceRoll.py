print("Dice and Roll Game")
import random


def DiceAndRoll():
    global inputs
    inputs = input("Roll the Dice y/n:" )
    inputs = inputs.lower()
    if inputs =='y' :
      print(tuple(random.sample(range(1,7),k = 2)))
      DiceAndRoll()
    elif inputs == 'n':
       print("thanks for playing")
    else:print("enter valid data")
DiceAndRoll()

# print(inputs)
print("This is A Rock Paper Sessiors Game Lets Play😁")
import random



def show(user_choice,com_choice):
  print(f"user choices :{user_choice} and the com_choices :{com_choice}")


def valid():
  global list
  list= ['rock','paper','sessiors']
  global game
  game= input("Enter r/p/s:").lower()

  if game not in ('r','p','s'):
    print("Ener a Vaid Char 🥱")
    return games()
  global user_choice
  user_choice= {'r':'rock','p':'paper','s':'sessiors'}[game]
  global com_choice
  com_choice = random.choice(list)
def checkWinner():
  if com_choice == user_choice:
    print("Ohh Shit Tie 😋")
    return games()
  elif (com_choice == list[1] and user_choice == list[2]) or \
        (com_choice == list[0] and user_choice ==list[1]) or \
        (com_choice ==  list[2] and user_choice == list[0]):
    print('user wins 😂')
  else:print("computer wins 🤣")

def playOrNot():
  continuee = input("Contuine y/n :").lower()
  if continuee == 'y':return games()
  elif continuee == 'n':return
  else :print("please type right options :")

def games():
  valid()
  show(user_choice,com_choice)
  checkWinner()
  playOrNot()

games()


import random
from urllib.parse import uses_relative

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
user_choice=int(input("You do you choose? 0 for rock or 1 for scissor or 2 for paper:"))
if user_choice >2 or user_choice<0:
    print("You entered an invalid number, You LOST..!")
elif user_choice==0:
    print("You choose Rock:"+rock)
elif user_choice==1:
    print("You choose Scissors:"+scissors)
else:
    print("You choose Paper:"+paper)
if user_choice<=2 and user_choice>=0:
    computer_choice = random.randint(0,2)
    print(f"Computer choice: {computer_choice}")
    if computer_choice==0:
        print("Computer choose Rock:"+rock)
    elif computer_choice==1:
        print("Computer choose Scissors:"+scissors)
    else:
        print("Computer choose Paper:"+paper)
    if user_choice == computer_choice:
        print("It is draw..!")
    elif (user_choice==0 and computer_choice==1) or \
         (user_choice==1 and computer_choice==2) or \
         (user_choice==2 and computer_choice==0):
        print("You WIN...")
    else:
        print("You lost the Game")
else:
    print("You lost the Game")

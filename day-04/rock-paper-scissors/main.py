import random

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

gameImages = [rock, paper, scissors]

user_choice = int(input("What do you chose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
print(gameImages[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(gameImages[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You type a invalid number, you lose!!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice > user_choice:
    print("You lose!")

elif computer_choice == user_choice:
    print("It's a draw.")
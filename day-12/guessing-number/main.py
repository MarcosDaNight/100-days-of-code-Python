from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
    if guess > answer:
        print("To high.")
        return turns - 1
    elif guess < answer:
        print("To low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")

    
#Make a function to set the difficult
def chose_difficulty():
    level = input("Choose a difficuty. Type 'easy' or 'hard': ")
    
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print(logo)
    answer = randint(1, 100)
    print(f"The answer: {answer}")
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    turns = chose_difficulty()
    
    guess = 0
    while guess != answer:
        print(f"You have {turns} attemps reaming to guess the number.")

        #Let the user guess a number
        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print("You lose all attempts. GAME OVER!")
            return

#Track the number of turns and reduce by 1 if they get it wrong

#Repeat the guessing functionality if they get it wrong
game()
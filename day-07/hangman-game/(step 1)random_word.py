#Step 1 
import random
import os

word_list = ["aardvark", "baboon", "camel"]

def verifyWord(word, letter):
    for l in word:
        if l == letter:
            print("Right")
        else:
            print("Wrong")


#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chose_word = random.choice(word_list)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
letter = input("Guess a letter: ").lower()
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
run_again = ""

while True:
    if run_again == "":
        verifyWord(chose_word, letter)
        run_again = input("This repl exited. run again? ").lower()
    elif run_again == "no":
        print("Bye!")
        break
    else:
        os.system('clear')
        chose_word = random.choice(word_list)
        letter = input("Guess a letter: ").lower()
        verifyWord(chose_word, letter)
        run_again = input("This repl exited. run again? ").lower()
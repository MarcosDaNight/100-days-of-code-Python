#Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

def verifyLetter(guess, letter):
    return guess == letter

def verifyDisplay(display, chosen_word, guess):
    
    for i in range(len(display)):
        if verifyLetter(guess, chosen_word[i]):
            display[i] = chosen_word[i]

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.

guess = input("Guess a letter: ").lower()
display = ["_" for i in range(len(chosen_word))]

#TODO-2: - Loop through each position in the chosen_word;
verifyDisplay(display, chosen_word, guess)
#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".

print(display)
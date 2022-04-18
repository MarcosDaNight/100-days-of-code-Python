#Step 5

import random
from xml.etree.ElementTree import tostringlist
from hangman_words import word_list
from hangman_art import stages, logo
#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

def verifyWrongLetter(wrong_letters, guess):
    awnser = True
    for l in wrong_letters:
        if guess in wrong_letters:
            awnser = False
    return awnser

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(logo)
print("\n\n")
#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
wrong_letters = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    
    print("\nWrong letters: ")
    print(*wrong_letters)
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        if guess not in wrong_letters:
            lives -= 1
        else:
            print(f"\nAttention, you chose again another wrong letter: '{guess}'\n")
        if verifyWrongLetter(wrong_letters, guess):
            print(f"This is letter '{guess}' don't be a part of the word")
            wrong_letters.append(guess)
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The word is '{chosen_word}'")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(stages[lives])
#Step 5

import random
from hangman_words import word_list
from hangman_art import stages, logo

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

    
    print("\nWrong letters: ")
    print(*wrong_letters)
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
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

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
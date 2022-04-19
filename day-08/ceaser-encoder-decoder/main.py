alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if not char in alphabet:
        end_text += char
    else:
        position = alphabet.index(char)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
        
  print(f"Here's the {cipher_direction}d result: {end_text}")

def verifyShift(shift):
    if shift > len(alphabet):
        return shift % len(alphabet)
    return shift

from art import logo
print(logo)

restart = "yes"
while restart == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(start_text=text, shift_amount=verifyShift(shift), cipher_direction=direction)
    restart = input("\nYou want restart the program?\n ").lower()

print("Bye")
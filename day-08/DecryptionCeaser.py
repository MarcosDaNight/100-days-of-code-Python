alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = verifyShift(position + shift_amount)
    cipher_text += alphabet[new_position]
  return cipher_text


def verifyShift(shift_amout):
    if shift_amout >= len(alphabet):
         shift_amout -= len(alphabet)
    return shift_amout

def decrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        cipher_text += alphabet[position - verifyShift(shift_amount)]
    return cipher_text

def cesarEncryption():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction == "encode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        print("The encode text is "+ encrypt(text, shift))
    elif direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        print("The decode text is " + decrypt(text, shift))
    else:
        print("Wrong chosen, please try again.\n")
       
        cesarEncryption()

cesarEncryption()
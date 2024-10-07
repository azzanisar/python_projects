alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from art import logo
print(logo)


#Creating a function that works both encryption and decryption

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    #we took this if statement out of the for loop because when we decode the same encoded
    #message it was mutiplying the shift amount with -1 again in the for loop
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:

        #if user types number or symbol or anything not in alphabet list
        #then we just string concatenate it into our output text
        if letter not in alphabet:
            output_text += letter

        #otherwise if the letter is in the alphabet then we continue
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")


# Restarting the program

should_continue = True
while should_continue:
      direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
      text = input("Type your message:\n").lower()
      shift = int(input("Type the shift number:\n"))

      caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

      restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
      if restart == "no":
          should_continue = False
          print("Goodbye")




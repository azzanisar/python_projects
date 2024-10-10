import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game !")
random_num = random.randint(1,100)
print("I'm thinking of a number between 1 and 100. ")
user_choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

while user_choice == 'easy':
     print(f"You have {EASY_ATTEMPTS} attempts remaining to guess the number.")
     guess = int(input("Make a guess: "))
     EASY_ATTEMPTS -= 1

     if random_num < guess:
        print("Too high.")
        print("Guess again.")

     elif random_num > guess:
        print("Too low.")
        print("Guess again.")

     elif random_num  == guess:
        print(f"You got it! The answer was {random_num}")
        break


     if EASY_ATTEMPTS == 0:
        print("You've run out of guesses, you lose.")
        break



while user_choice == 'hard':
    print(f"You have {HARD_ATTEMPTS} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    HARD_ATTEMPTS -= 1

    if random_num < guess:
        print("Too high.")
        print("Guess again.")

    elif random_num > guess:
        print("Too low.")
        print("Guess again.")

    elif random_num == guess:
        print(f"You got it! The answer was {random_num}")
        break #break statement exit the loop entirely here


    if HARD_ATTEMPTS == 0:
        print("You've run out of guesses, you lose.")
        break #if you have zero attempts, break or exit the loop





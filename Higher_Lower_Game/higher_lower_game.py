from art import logo,vs
from game_data import data
import random


""" data is a list with dictionaries as its items so first we access random index and
 then we print their details in a statement"""

#Step-1: Function to get random data account
def get_random_data():
    """Gets random index from data list which is the celeb account as dictionary"""
    random_account =  random.choice(data)
    return random_account

#Step-2: Format celeb data into description
def format_data(account):
    """Getting description of the random data index"""
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, a {description}, from {country}"

#Step-3: Check user's guess against correct answer
def check_answer(u_guess,a_follower, b_follower):
    """Checks user's guess against the followers count and returns True if they got it right
    or False if they got it wrong"""
    if a_follower > b_follower:
        return u_guess == 'a' #if A has more followers than B and user guessed A then return True
    else:
        return u_guess == 'b'

#Step-4: If user got it right, make previous B as the new A
#Repeat process and add up score until user gets it wrong
def game():
    """How the game works"""
    print(logo)
    user_score = 0
    game_continues = True

    account_b = get_random_data() #gets random account to B

    while game_continues:
        account_a = account_b #making previous B as new A if user got it right
        account_b = get_random_data() #and the new B will get new random data account

        if account_a == account_b:
            """When user gets it right, we keep repeating the process to make A as 
            previous B and new B gets new random account"""
            account_b = get_random_data()

            print(f"Compare A: {format_data(account_a)}")
            print(vs)
            print(f"Against B: {format_data(account_b)}")
            guess = input("Who has more followers? Type 'A' or 'B': ").lower()
            a_follower_count = account_a['follower_count']
            b_follower_count = account_b['follower_count']

            answer = check_answer(u_guess=guess, a_follower=a_follower_count,b_follower=b_follower_count)

            print(logo)
            if answer:
                """If answer is correct as the user's guess then we increase user's score by 1"""
                user_score += 1
                print(f"You're right! Current score: {user_score}")

            else:
                print(f"Sorry, that's wrong. Final score: {user_score}")
                game_continues = False


game()









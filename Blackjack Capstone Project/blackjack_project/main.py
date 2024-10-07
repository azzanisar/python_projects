import random
import art

#Function to get random card from our cards list
def deal_card():
    """return random card from deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card


#Function to calculate score of user and computer
def calculate_score(cards):
    score = sum(cards)
    """Takes a list of cards and returns the score calculated """
    if score == 21 and len(cards) == 2:
        return 0 # 0 represents blackjack

    if 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)

    return score



def compare(u_score, c_score):
    if u_score == c_score:
        return "It's a draw."
    elif c_score == 0:
        return "You lose, opponent has BlackJack."
    elif u_score == 0:
        return "You win with a BlackJack."
    elif u_score > 21:
        return "You lose, you went over"
    elif c_score > 21:
        return "Opponent went over, you win"
    elif u_score > c_score:
        return "You won"
    else:
        return "You lose"

def play_game():
    print(art.logo)
    user_cards = []
    computer_cards = []

    #We are setting these variables outside while loops so we can use them anywhere
    computer_score = -1
    user_score = -1
    #This condition is the game is not over so it is false
    is_game_over = False


    """This for loop will run 2 times and append 
     2 cards in user card and computer card"""
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    #this while loop is for user so they can take cards
    while not is_game_over:

        #We are calling calculate function after we have given 2 cards to user and computer
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")


        #Hint:9 when these conditions are met, then game ends and we set it to True
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_choice == 'y':
                #When user chooses another card from the card deck, we append that to user_card list
                user_cards.append(deal_card())
            else:
               is_game_over = True



    #If the computer score is less than 17, computer keeps drawing the cards
    #this while loop is for computer, so the dealer can handle strategy
    while computer_score != 0 and computer_score < 17:
           computer_cards.append(deal_card())
           computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score,computer_score))


while input("Do you want to play a game of BlackJack? Type 'y' or 'n': ") == 'y':
    #it plays all the part from empty user cards list to the end of comparison
    print('\n' * 20)
    play_game()








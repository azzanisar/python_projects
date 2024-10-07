from art import logo
print(logo)

"""
Making a separate function to find the highest bidder
and using a for loop to loop through the dict
so we loop through the keys which is the names in bid dict
and we get the value\price as the bid_amount
"""

#we could also use max() function
#max(bidding_dict, key=bidding_dict.get)
def highest_bid(bidding_dict):
    winner =""
    highest_bid_num = 0
    for bidder in bidding_dict:
          bid_amount = bidding_dict[bidder]
          #finding highest bidder like highest score
          #then we make the winner as that bidder
          if bid_amount > highest_bid_num:
                highest_bid_num= bid_amount
                winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid_num}.")


"""
 Keeping the bids dict outside the while loop so that it accumulates
the key and values and it doesn't become zero everytime the while loop runs 
so if it was inside the while loop, everytime it would become empty 
"""

bids = {}
continue_bidding = True
while continue_bidding:
      name = input("What is your name? ")
      price = int(input("What is your bid? $ "))
      bids[name]= price
      print(bids)
      should_continue = input("Are there any new bidders? Type 'yes' or 'no .\n").lower()

      if should_continue == "no":
          #If there are no other bidders, then while loop should end
          #and continue_bidding becomes False
          continue_bidding = False
          highest_bid(bids)

      elif should_continue == "yes":
          print("\n" * 20)
          #now it will loop through back to the while loop
          #and ask user name and bid price








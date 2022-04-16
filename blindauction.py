import os
from art import logo

auction_dict = {}

auction = True
print(logo)
while auction:
    name = input("\nEnter your name: ")
    while True:
        try:
            bid = float(input("\nEnter your bid: $"))
        except ValueError:
            print("\nBid must be a number - try again")
        else:
            break
    auction_dict[name] = bid
    winner = ""
    continue_ask = input("\nAre there more bidders? ").lower()
    if continue_ask == "no" or continue_ask == "n":   
        winning_bid = 0
        for x in auction_dict:
            high_current = auction_dict[x]
            if high_current > winning_bid:
                winner = x
        winning_bid = "{:0.2f}.".format(high_current)
        print(f"\nThe winner is {winner} with a winning bid of ${winning_bid}")
        auction = False
    else:
        os.system('clear')
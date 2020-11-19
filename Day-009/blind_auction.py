import art
from replit import clear
#HINT: You can call clear() to clear the output in the console.

# Show logo from art.py
print(art.logo)

# Make sure the while loop executes at least once
bidders = "yes"

while bidders == "yes":
  # Ask for name input
  name = input("What is your name?\n")

  # Ask for bid price
  bid = input("What is your bid? $")

  # Add name and bid into dictionary
  bid_dict = {}
  bid_dict[name] = bid

  # Ask if there are other users who want to bid
  bidders = input("Are there other users that want to bid? (yes/no)\n").lower()

  # Clear screen
  clear()

# If there are no other bidders, find the highest bidder and declare it as winner
if bidders == "no":
  # Assume first entry is the highest bidder
  highest_bidder_name = list(bid_dict.keys())[0]
  highest_bidder_bid = bid_dict[highest_bidder_name]

  # Find highest bidder
  for key in bid_dict:
    if bid_dict[key] > highest_bidder_bid:
      highest_bidder_name = key
      highest_bidder_bid = bid_dict[key]

  print(f"The winner is {highest_bidder_name} with a bid of ${highest_bidder_bid}.")

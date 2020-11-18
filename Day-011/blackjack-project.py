############### Blackjack Project #####################

#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################################################
from art import logo
from replit import clear
import random

# Store all possibilities of cards in an array
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Store all possibilities of results in an array
results = [
  "You lose 😭", 
  "You went over. You lose 😭", 
  "Win with a Blackjack 😎", 
  "Draw! 🙃",
  "Win! 😎"
]

play_game = True

while play_game:
  if input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    # Clear screen and print logo
    clear()
    print(logo)

    # Create dict to store cards and values
    cards_dealt = {
      "user": [],
      "computer": [],
    }

    # Deal first 2 cards to user and to computer
    for i in range(2):
      cards_dealt["user"].append(cards[random.randint(0, 12)])
      cards_dealt["computer"].append(cards[random.randint(0, 12)])

    # Make sure you don't get 2 A's
    if cards_dealt["user"][0] == cards_dealt["user"][1] and cards_dealt["user"][1] == 11:
      cards_dealt["user"][1] = 1
    if cards_dealt["computer"][0] == cards_dealt["computer"][1] and cards_dealt["computer"][1] == 11:
      cards_dealt["computer"][1] = 1

    # Keep track if you need to play another card
    play_another_card = True

    while play_another_card:
      # Calculate current score
      current_score_user = 0
      current_score_computer = 0
      for i in range(len(cards_dealt["user"])):
        current_score_user += cards_dealt["user"][i]
        current_score_computer += cards_dealt["computer"][i]

      # Display current score
      print(f"     Your cards: {cards_dealt['user']}, current score: {current_score_user}")
      print(f"     Computer's first card: {cards_dealt['computer'][0]}")

      # If user over 21, bust without deal
      if current_score_user > 21:
        play_another_card = False
        result = 1

      # If user has 21, blackjack without deal
      elif current_score_user == 21:
        play_another_card = False
        result = 2
      
      # If user has below 21 he can choose to deal or pass
      else:
        if input("Type 'y' to get another card, type 'n' to pass: ").lower() == "y":
          cards_dealt["user"].append(cards[random.randint(0, 12)])
          
          # If the card is A and the score is already over 11, it's a 1
          if cards_dealt["user"][-1] == 11 and current_score_user > 10:
            cards_dealt["user"][-1] = 1
          cards_dealt["computer"].append(cards[random.randint(0, 12)])
          if cards_dealt["computer"][-1] == 11 and current_score_computer > 10:
            cards_dealt["computer"][-1] = 1
        
        # If user has under 21 and he passes
        else:
          
          # If user score is below computer score he loses
          if current_score_user < current_score_computer:
            result = 0
          
          # If computer has under player and under 21, computer deals until over player or bust
          while current_score_computer <= current_score_user and current_score_computer < 21:
            cards_dealt["computer"].append(cards[random.randint(0, 12)])

            # Make sure an A is == 1
            if cards_dealt["computer"][-1] == 11 and current_score_computer > 10:
              cards_dealt["computer"][-1] = 1

            # Calculate current computer score
            current_score_computer = 0
            for i in range(len(cards_dealt["computer"])):
              current_score_computer += cards_dealt["computer"][i]
            
            # If computer score is > 21 it's a bust
            if current_score_computer > 21:
              result = 4

            # Else computer wins
            else:
              result = 0

          play_another_card = False

    # Print final results
    print(f"Your final hand: {cards_dealt['user']}, final score: {current_score_user}")
    print(f"Computer's final hand: {cards_dealt['computer']}, final score: {current_score_computer}")
    print(results[result])

  else:
    play_game = False

print("\nBye-bye!")

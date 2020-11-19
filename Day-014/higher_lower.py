## Higher Lower Game. Compare who has more IG followers
# Import modules
from art import logo, vs
from replit import clear
from game_data import data
import random


def introduction():
  '''
  Make the introduction screen. Clear everything and print the logo
  '''
  # Clear screen
  clear()
  # Print logo
  print(logo)


def increment_score(player_score):
  '''
  Increments the player's score
  '''
  player_score += 1
  return player_score


def pick():
  '''
  Function that asks the user to pick between 'A' or 'B' and returns the player's choice.
  '''
  # Ask user to guess
  a_or_b = ["a", "b"]
  player_pick = 0
  while player_pick not in a_or_b:
    try:
      player_pick = input("Who has more followers? Type 'A' or 'B': ").lower()
    except ValueError:
      pass
  return player_pick


def display_options(option_a, option_b):
  '''
  Prints the options for the player to pick from.
  '''
  print(f"Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}")
  print(vs)
  print(f"Compare A: {option_b['name']}, a {option_b['description']}, from {option_b['country']}")


def main():
  '''
  Main executable function of the program.
  '''
  introduction()

  # Keep score
  player_score = 0

  # Pick 2 random entries to compare
  option_a = random.choice(data)

  end_game = False
  while not end_game:
    option_b = random.choice(data)
    while option_a == option_b:
      option_b = random.choice(data)

    # Display comparing options
    display_options(option_a, option_b)

    #Ask user to pick
    player_pick = pick()
    
    # Test if player got it right
    if player_pick == "a":
      if option_a['follower_count'] < option_b['follower_count']:
        result = 0
        end_game = True
      else:
        result = 1
        player_score = increment_score(player_score)
        introduction()
        print(f"You're right! Current score: {player_score}.")
    else:
      if option_a['follower_count'] > option_b['follower_count']:
        result = 0
        end_game = True
      else:
        result = 1
        player_score = increment_score(player_score)
        introduction()
        print(f"You're right! Current score: {player_score}.")
        option_a = option_b

    if result == 0:
      introduction()
      print(f"Sorry, that's wrong. Final score: {player_score}.")



# Run main function if program executes
if __name__ == "__main__":
  main()

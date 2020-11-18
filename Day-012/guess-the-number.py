# Guess the number game
from art import logo, yay, oh_no
import random
from replit import clear

def introduction():
  """
  Function that prints the intro message at the beginning of the game and returns random number [1, 100]
  """
  clear()
  print(logo)
  print("Welcome to the Guessing Number Game!")
  print("I'm thinking of a number between 1 and 100.")

  return random.randint(1, 100)


def difficulty():
  """
  Function that selects difficulty level and returns initial tries
  """
  difficulties = ["easy", "hard"]
  player_level = 0

  # Handle any other input than easy or hard
  while player_level not in difficulties:
    player_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  
  if player_level == "easy":
    tries = 10
  else:
    tries = 5

  return tries


def guess_number():
  '''
  Asks user to guess an integer between 1 and 100
  '''
  guess_ok = False
  while not guess_ok:
    try:
      guess = int(input("Make a guess: "))
      if guess > 0 and guess <= 100:
        guess_ok = True
      else:
        print("Your guess is not a number between 1 and 100.")
    except ValueError:
      print("Your guess is not a number between 1 and 100.")

  return guess


def compare(guess, number):
  '''
  Compare guessed number with the random number.
  '''
  if guess < number:
    return 1
  elif guess > number:
    return 2
  else:
    return 3


def play_again():
  print("\n")
  play_options = ["y", "n"]
  play_select = 0
  while play_select not in play_options:
    play_select = input("Play again? [y/n] ").lower()

  if play_select == "y":
    return main()


def main():
  ## Introduction message
  ## Generate the number
  number = introduction()

  ## Choose difficulty
  tries_left = difficulty()

  while tries_left > 0:
    print("\n")
    ## Tell user how many attempts he has left
    print(f"You have {tries_left} attempts remaining to guess the number.")

    ## Ask user to make a Guess
    guess = guess_number()

    ## Tell user if guess is too low or too high
    if compare(guess, number) == 1:
      print("Too low.")
      print("Guess again.")
    elif compare(guess, number) == 2:
      print("Too high.")
      print("Guess again.")
    else:
      print(yay)
      print(f"You got it! The answer is {guess}")
      break
    
    tries_left -= 1

  ## If number of guesses ran out, game over
  if tries_left == 0:
    print(oh_no)
    print("You've run out of guesses, you lose.")

  play_again()


if __name__ == main():
  main()

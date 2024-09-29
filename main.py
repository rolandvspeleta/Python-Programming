import time

from hangman import *
from random_guessing import *
from rps import rps_game
from slot import slot_machine


def main():

  continue_playing = True
  programs = ("a. RPS", "b. Number Guessing", "c. Slot Machine", "d. Hangman", "z. Exit Python")
  
  while continue_playing:
    print()
    print("Programs")
    for program in programs:
      print(program)
    game = input("What do you want?: ")
    print()

    
    if game == "a":
      rps_game()

    elif game == "b":
      number_guessing()


    elif game == "c":
    
      slot_machine()
      
    elif game == "d":
      hangman()
      
    elif game == "z":
      print("EXITING PYTHON.........")
      time.sleep(2)
      continue_playing = False

    else:
      print(f"Invalid! No game in choice {game.upper()}")
      continue_playing = True

  
if __name__ == '__main__':
  main()
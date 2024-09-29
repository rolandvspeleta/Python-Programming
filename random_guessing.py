import random


def guessing_condition(guesses):
  pass
    
def exit_game():
  
  play_again = input("Play again? y/n: ").lower()
  if not play_again == "y":
    return False
  else:
    return True
  
def number_guessing():
  running = True
  lowest_num = 1
  highest_num = 1000
  answer = random.randint(lowest_num, highest_num)
  guesses = 0

  while running:
      
    not_guessed = True
    print("Python Number Guessing Game")
    print("Select number between 1 to 1000")

    while not_guessed:
      
      guess = input("Enter your guess: ")

      if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < lowest_num or guess > highest_num:
          print("Guess out of range")
          print("Please select number between 1 to 100")
        elif guess < answer:
          print("Too low!")
        elif guess > answer:
          print("Too high")
        else:
          print(f"Correct! The answer was: {guess}")
          print(f"The number of guesses: {guesses}")
          running = exit_game()
      else:
        print("Invalid guess")
        print("Please select number between 1 to 1000")
            
    
if __name__ == '__main__':
  number_guessing()
import random


def win_condition(player, computer):
  
    if player == computer:
      print("It's a tie! ")
      return "Game Draw"
    elif player == "🪨" and computer == "✂️":
      return "Player Win"
    elif player == "📃" and computer == "🪨":
      return "Player Win"
    elif player == "✂️" and computer == "📃":
      return "Player Win"
    else:
      print("Computer wins!")
      return "Computer Win"
  
def show_score(computer_score, player_score, draws):
  print(f"Computer Score: {computer_score}")
  print(f"Player Score: {player_score}")
  print(f"Draws: {draws}")

def rps_game():
  
  options = ("🪨", "📃", "✂️")
  running = True
  player_score = 0
  computer_score = 0
  draws = 0
  game_on = True
  
  while game_on:
    
    race_to = input("RPS Game Race to (enter a number)?: ")
    
    if race_to.isdigit():
      race_to = int(race_to)
      print()
      print(f"RPS Game Race to {race_to}")
      
      while running:

        player = None
        computer = random.choice(options)
        
        while player not in options:
          
          player = input("Enter rock or paper or scissors: ")
          if player == "rock":
            player = "🪨"
          elif player == "paper":
            player = "📃"
          elif player == "scissor":
            player = "✂️"
          else: 
            print("Only rock, paper, scissors")
        print(f"Player: {player}")
        print(f"Computer: {computer}")
              
        score = win_condition(player, computer)
        if score == "Player Win":
          player_score += 1
          print(f"Player {player_score} : {computer_score} Computer")
          if player_score == race_to:
            print("Player Wins!!!")
            game_on = False
            break
        elif score == "Computer Win":
          computer_score += 1
          print(f"Player {player_score} : {computer_score} Computer")
          if computer_score == race_to:
            print("Computer Wins!!!")
            game_on = False
            break
        elif score == "Game Draw":
          draws += 1
    else:
      print("That is not a number")
      
  
  
if __name__ == '__main__':
  rps_game()
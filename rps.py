import random


def win_condition(player, computer):
  
    if player == computer:
      print("It's a tie! ")
      return "Game Draw"
    elif player == "🪨" and computer == "✂️":
      print("Player win!")
      return "Player Win"
    elif player == "📃" and computer == "🪨":
      print("Player win!")
      return "Player Win"
    elif player == "✂️" and computer == "📃":
      print("Player wins!")
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
    elif score == "Computer Win":
      computer_score += 1
    elif score == "Game Draw":
      draws += 1

    playing_again = True
    
    while playing_again:
      
      play_again = input("Enter to play again (s: see score q: quit): ").lower() 
      if play_again == "q":
        running = False
        playing_again = False
      elif play_again == "s":
        show_score(computer_score, player_score, draws)
      else:
        playing_again = False

if __name__ == '__main__':
  rps_game()
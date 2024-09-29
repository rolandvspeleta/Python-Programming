import random
import time


def spin_row():
  symbols = ['😂', '😂', '😂', '😂', '😂', '😊', '😊', '😊', '😊', '😍', '😍', '😍', '👍', '👍', '⭐']
  results = []
  for symbol in range(3):
    results.append(random.choice(symbols))
  return results
def print_row(row):
  print(" | ".join(row))
  print("-------------")

def get_payout(row, bet):
  if row[0] == row[1] == row[2]:
    if row[0] == '😂':
      return bet * 2
    elif row[0] == '😊':
      return bet * 3
    elif row[0] == '😍':
      return bet * 5
    elif row[0] == '👍':
      return bet * 10
    elif row[0] == '⭐':
      return bet * 20
  return 0

def slot_machine():
  
  balance = 100
  print("**********************")
  print("Welcome to Python Slot")
  print("**********************")
  print("Symbols: 😂 😊 😍 👍 ⭐")
  print("**********************")

  while balance > 0:

      print(f"Current Balance: ${balance}")

      bet = input("Place your bet amount: ")

      if not bet.isdigit():
        print("Bet Invalid")
        continue

      bet = int(bet)

      if bet > balance:
        print("Insufficient Funds")
        continue
      
      if bet <= 0:
        print("Bet Invalid")
        continue

      balance -= bet
      row1 = spin_row()
      row2 = spin_row()
      row3 = spin_row()
      print("Spinning...\n")
      time.sleep(0.5)
      print_row(row1)
      time.sleep(1)
      print_row(row2)
      time.sleep(1)
      print_row(row3)
      
      payout = get_payout(row1, bet) + get_payout(row2, bet) + get_payout(row3, bet)
      if payout > 0:
        print(f"You won ${payout}")
      else: print("Sorry you lost this round")

      balance += payout
      play_again = input("Do you want to spin again? (y/n): ").lower()
      if not play_again == 'y':
        break
      else:
        continue
  else:
    print("Zero Funds, Returning to Main Screen")
    time.sleep(1)

      

if __name__ == '__main__':
  slot_machine()
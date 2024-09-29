
def show_balance(balance):
  print()
  print(f"Balance: ${balance}")
  print()

def deposit():
  deposit_amount = float(input("Enter amount you want to deposit: $"))
  return deposit_amount


def withdraw(balance):
  withdraw_amount = float(input("Enter amount you want to withdraw: $"))
  if  withdraw_amount > balance:
    print("Insufficent Funds")
    return 0
  elif  withdraw_amount< 0:
    print("Withdrawing $0")
    return 0
  else:
    return withdraw_amount
  
def main(balance):

  balance = 1000
  is_running = True

  while is_running:
    print("Banking Program")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
      show_balance(balance)
    elif choice == 2:
      balance += deposit()
    elif choice == 3:
      balance -= withdraw(balance)
    elif choice == 4:
      is_running = False
    else:
      print("Not Valid")

if __name__ == '__main__':
  main()
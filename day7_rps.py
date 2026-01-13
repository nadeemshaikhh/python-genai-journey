import random

choices = ["rock", "paper", "scissors"]

def get_user_choice():
  while True:
    user = input("Choose rock, paper, scissors (or 'quit'): ").lower()
    if user == "quit":
      return "quit"
    if user not in choices:
      print("Invalid choice. Try again.")
      continue
    return user
    
def get_computer_choice():
  return random.choice(choices)

def decide_winner(user, computer):
  if user == computer:
      return "It's a tie!"
  elif user == "rock" and computer == "scissors":
      return "You win!"
  elif user == "paper" and computer == "rock":
      return "You win!"
  elif user == "scissors" and computer == "paper":
      return "You win!"
  else:
      return "You lose!"
    
def main():
  print("Rock Paper Scissors Game")
  while True:
    user = get_user_choice()
    if user == "quit":
      print("Thanks for playing!")
      break
    computer = get_computer_choice()
    print("You chose:", user)
    print("Computer chose:", computer)
    
    result = decide_winner(user, computer)
    print(result)
    print("------------------")

main()

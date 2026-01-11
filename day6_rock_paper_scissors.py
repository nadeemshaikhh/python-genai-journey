import random

choices = ["rock","paper","scissors"]

user = input("Choose rock, paper, scissors: ").lower()
if user not in choices:
  print("Invalid choice! Please run the game again and choose correctly.")
  exit()
computer = random.choice(choices)

print("You chose:", user)
print("Computer chose:", computer)

if user == computer:
  print("It's a tie")
elif user == "rock" and computer == "scissors":
  print("You win!")
elif user == "paper" and computer == "rock":
  print("You win!")
elif user == "scissors" and computer == "paper":
  print("You win!")
else:
  print("You lose!")

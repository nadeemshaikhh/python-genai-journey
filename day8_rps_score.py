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
        return "tie"
    elif user == "rock" and computer == "scissors":
        return "user"
    elif user == "paper" and computer == "rock":
        return "user"
    elif user == "scissors" and computer == "paper":
        return "user"
    else:
        return "computer"

def main():
    user_score = 0
    computer_score = 0

    print("🎮 Rock Paper Scissors Game with Score")

    while True:
        user = get_user_choice()
        if user == "quit":
            print("Thanks for playing!")
            print("Final Score:")
            print("You:", user_score, "Computer:", computer_score)
            break

        computer = get_computer_choice()

        print("You chose:", user)
        print("Computer chose:", computer)

        winner = decide_winner(user, computer)

        if winner == "tie":
            print("It's a tie!")
        elif winner == "user":
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print("Score => You:", user_score, "| Computer:", computer_score)
        print("----------------------------")

main()

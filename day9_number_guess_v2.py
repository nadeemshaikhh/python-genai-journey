import random

def play_game():
  secret = random.randint(1, 10)
  attempts = 0
  print("Number Guessing Game")
  print("I am thinking of a number between 1 and 10.")
  print("Type 'quit' to exit.")
  
  while True:
    user_input = input("Enter your guess: ")
    
    if user_input.lower() == "quit":
      print("You quit the game. The number was:", secret)
      break
    
    if not user_input.isdigit():
      print("Please enter a valid number.")
      continue
    
    guess = int(user_input)
    attempts += 1
    
    if guess < secret:
            print("Too low! Try again.")
    elif guess > secret:
            print("Too high! Try again.")
    else:
            print("🎉 Correct! You guessed it in", attempts, "attempts.")
            break
play_game()
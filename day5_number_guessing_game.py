secret = 7
guess = 0
  
while guess != secret:
  guess = int(input("Guess the number (1-10): "))
  if guess == secret:
    print("Correct! You guessed it!")
  else:
    print("Wrong, try again!")
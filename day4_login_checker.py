age = 18

if age >= 18:
  print("Adult")
else:
  print("Minor")
  
marks = 75

if marks >= 90:
  print("Grade A")
elif marks >= 60:
  print("Grade B")
else:
  print("Grade C")
  
age = int(input("Enter your age: "))
if age >= 18:
  print("You can vote")
else:
  print("You cannot vote")
  
saved_password = "1234"
user_password = input("Entre password:")
if user_password == saved_password:
  print("Login sucessful")
else:
  print("Wrong password")
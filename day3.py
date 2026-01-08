def add(a,b):
  return a+b
def sub(a,b):
  return a-b
def mul(a,b):
  return a*b
def div(a,b):
  return a/b

print("Simple Calculator")
print("1. Add")
print("2. Sub")
print("3. Mul")
print("4. Div")

choice = input("Enter your choice (1/2/3/4): ")
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))

if choice =="1":
  print("Result:", add(num1, num2))
elif choice =="2":
  print("Result:", sub(num1, num2))
elif choice =="3":
  print("Result:", mul(num1, num2))
elif choice =="4":
  print("Result:", div(num1, num2))
else:
  print("Invalid choice")
import time
from art import logo



user_repeat = True

def add(n1,n2):
  return n1 + n2

def subtract(n1,n2):
  return n1 - n2

def multiply(n1,n2):
  return n1 * n2

def divide(n1,n2):
  return n1/n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
while user_repeat == True:
  print("\033c")
  print(logo)
  print("Welcome to the calculator!")
  num1 = input("What is the first number? ")
  num2 = input("What is the second number? ")
  numeric_repeat = True
  if num1.isnumeric() == True or num2.isnumeric() == True or num1.isdigit() == True or num2.isdigit() == True:
    num1 = float(num1)
    num2 = float(num2)
    op_symbol = 0
    op_symbol = input("What operation do you want to undergo?  " + " ".join(operations) +"  :")
    if op_symbol == 0:
      print("Invalid operation")
    else:
  
  
      def answer(num1,num2,op_symbol):
        op = operations.get(op_symbol)
        result = 0 
        if op == add:
          result = add(num1,num2)
        elif op == subtract:
          result = subtract(num1,num2)
        elif op == multiply:
          result = multiply(num1,num2)
        elif op == divide:
          result = divide(num1,num2)
        else:
          result = "Invalid operation"
        return result
    
      finalanswer = answer(num1,num2,op_symbol)
      
      if finalanswer != "Invalid operation":
        print(f"{num1} {op_symbol} {num2} = {finalanswer}")
        x = input("Do you want to continue?  Y or N ").lower()
      else:
        print("Invalid operation")
        x = input("Do you want to continue?  Y or N ").lower()
      
      if x == "y":
        user_repeat = True
      else:
        user_repeat = False
  else:
    print("One of your numbers is not a number. Please try again.")
    time.sleep(2)
  
else:
  print("\033c")
  print(logo)
  print("Thank you for using the program.")



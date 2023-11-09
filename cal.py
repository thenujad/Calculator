#TODO: Write the functions for arithmatic operations here
#These functions should cover Task 2
def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        print("float division by zero")
        return 'None'
    return a / b

def power(a,b):
    return a ** b
   
def remainder(a,b):
    if b == 0:
        print("Error: Division by zero")
        return 'None'
    return a % b


#-------------------------------------
#TODO: Write the select_op(choice) function here
#This function sould cover Task 1 (Section 2) and Task 3

def select_op(choice):
    if choice == '+':
        print(choice)
        return add
    elif choice == '-':
        print(choice)
        return subtract
    elif choice == '*':
        print(choice)
        return multiply
    elif choice == '/':
        print(choice)
        return divide
    elif choice == '^':
        print(choice)
        return power
    elif choice == '%':
        print(choice)
        return remainder
    elif choice == '#':
        print(choice)
        return None
    elif choice == '$':
        print(choice)
        return 'reset'
    else:
        print("Unrecognized operation")
        return None


#End the select_op(choice) function here
#-------------------------------------
#This is the main loop. It covers Task 1 (Section 1)
#YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE
while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  

  # take input from the user
  choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
  
  if choice == '#':
    #program ends here
    print(choice)
    print("Done. Terminating")
    break 
  elif choice == '$':
      print(choice)
      continue
  elif choice not in ['+', '-', '*', '/', '^', '%', '#', '$']:
      print(choice)
      print("Unrecognized operation")
      continue
   
  operation = select_op(choice)
  
  if operation:
      n1 = input("Enter first number: ")
      print(n1)
      if "#" in n1:
          print("Done. Terminating")
          break
      if "$" in n1:
          continue

      n2 = input("Enter second number: ")
      print(n2)
      if "#" in n2:
          print("Done. Terminating")
          break
      if "$" in n2:
          continue
      try:

          a = float(n1)
          b = float(n2)
      except ValueError:
          print("Not a valid number, please enter again")
          continue

      result = operation(a, b)
      if result is not None:
          print(f"{a} {choice} {b} = {result}")
      else:
          print(f"{a} {choice} {b} = None")
exit()
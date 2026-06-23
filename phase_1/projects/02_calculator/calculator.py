def add(a,b):
 return a+b

def subtract(a,b):
  return a-b

def divide(a,b):
  if b == 0:
    return "error"
  return float(a/b)

def multiply(a,b):
  return a*b

def calculate(operation,num1,num2):
  if operation =="add":
    return add(num1,num2)
  elif operation =="subtract":
    return subtract(num1,num2)
  elif operation =="divide":
    return divide(num1,num2)
  elif operation == "multiply":
    return multiply(num1,num2)
  else:
    return "unknown operation"
while True:
   user_operation= input("what operation do you want to do (add,subtract,divide,multiply) quit to stop")
   if user_operation=="quit":
     break
   try:
    user_first_num=int(input("enter your first number"))
   except ValueError:
    print("enter valid number")
    continue
   try:
    user_second_num=int(input("enter your second number"))
   except ValueError:
    print("enter valid number")
    continue
   print(calculate(user_operation,user_first_num,user_second_num))


  





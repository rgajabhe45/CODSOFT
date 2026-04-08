# calculator program 
print("Simple Calculator") 

a = int(input("Enter first Number: "))
b = int(input("Enter second Number: "))

print("Choose Operation: ")
print("1 - Add ")
print("2 - Subtraction")
print("3 - Multiply")
print("4 - Divide")

option = input("Enter your Choice: ")

if option == '1':
  ans = a + b
  print("Addition =", ans)
  
elif option == '2':
  ans = a - b 
  print("Subtraction =", ans)
  
elif option == '3':
  ans = a * b
  print("Multiplication =", ans)
elif option == '4':
  if b != 0:
    ans = a / b
    print("Division =", ans)
  else:
    print("Cannot divide by zero")

else:
  print("Wrong Choice")
  
  
  
  



       
  

  
  

        
        

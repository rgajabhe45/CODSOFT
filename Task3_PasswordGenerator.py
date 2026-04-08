# Password Generator Program 

import random 
import string 

print("Welcome to Password Generator")

length = int(input("Enter the length of password:"))
all_chars = string.ascii_letters + string.digits + string.punctuation
generated_password = ""

for i in range(length):
  ch = random.choice(all_chars)
  generated_password = generated_password + ch

print("Generated Password:", generated_password)
             

"""Print numbers divisible by 3 or 5 from 
1 to 20 using a for loop

"""

for i in range(1,21):
    if i%3==0 or i%5==0:
        print(i)



"""Print numbers from 1 to 10. If a number is divisible by 4, 
stop the loop using a for loop and break statement:

"""


for i in range(1,11):

    if i%4==0:
        break
    print(i)



"""Python program that accepts a word 
from the user and reverses it.

"""
word = input("Enter a word: ")

reversed_word = word[::-1]

print("Reversed word:", reversed_word)



"""Python program to check if a given
 number is an Armstrong number

"""
number=int(input("Enter a number:"))
ord=len(str(number))
temp=number
sum=0
while(temp>0):
    digit=temp%10
    sum=sum+digit**ord
    temp=temp//10
if number==sum:
    print(f"{number} is an armstrong number")
else:
    print(f"{number} is  not an armstrong number")




"""Python program to display all numbers 
within a range except the prime numbers.

"""

n=int(input("Enter the limit :"))
for i in range(1,n+1):
    if i==1:
        continue
    for j in range(2,i):
        if i%j==0:
            print(i)
            break


# """Python program to check the validity of 
# password input by users.Password should not contain any space.
# Password should contain at least one digit(0-9).
# Password length should be between 8 to 15 characters.
# Password should contain at least one lowercase letter(a-z).

# """


# # password=input("Enter your password")
# # list1=password
# # ord=len(str(list1))
# # if ord<8 or ord>15:
# #     print("password is not valid")
# # elif 

# # # print(list1)



# import re

# # User input
# password = input("Enter your password: ")

# # Define password criteria
# min_length = 8
# max_length = 20

# # Initialize validity flag
# is_valid = True
# message = ""

# # Check length
# if len(password) < min_length or len(password) > max_length:
#     is_valid = False
#     message = "Password must be between 8 and 20 characters long."

# # Check for at least one uppercase letter
# if is_valid and not re.search(r'[A-Z]', password):
#     is_valid = False
#     message = "Password must contain at least one uppercase letter."

# # Check for at least one lowercase letter
# if is_valid and not re.search(r'[a-z]', password):
#     is_valid = False
#     message = "Password must contain at least one lowercase letter."

# # Check for at least one digit
# if is_valid and not re.search(r'[0-9]', password):
#     is_valid = False
#     message = "Password must contain at least one digit."

# # Check for at least one special character
# special_characters = r'[\W_]'  # Matches any non-alphanumeric character or underscore
# if is_valid and not re.search(special_characters, password):
#     is_valid = False
#     message = "Password must contain at least one special character."

# # Output the result
# if is_valid:
#     print("Password is valid.")
# else:
#     print(f"Invalid password: {message}")




"""Count the total numb er of digits in a number

"""


n=int(input("Enter a number"))
number=str(abs(n))
print(len(number))





"""a, b, c = 0, 0, 0 . Write a python program to print all 
permutations using those three variables

"""

for i in range(10):
    for j in range(10):
        for k in range(10):
            print(f"{i},{j},{k}")

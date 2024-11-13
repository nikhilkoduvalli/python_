




# """Write a Python program to check if a given string is a valid identifier
#  or not. An identifier is valid if it starts with a letter (a-z, A-Z) or
#  an underscore (_) followed by zero or more letters,
#    underscores, or digits (0-9)."""

# string1=input("Enter a string:")
# ans=string1.isidentifier()
# if ans==True:
#     print(f"{string1} is an identifire")
# else:
#     print(f"{string1} is not an identifire")


# """Write a Python program that takes three numbers as input
#  from the user and prints out the sum of those numbers."""


# num1=int(input("Enter a number:"))
# num2=int(input("Enter 2nd number:"))
# num3=int(input("Enter 3rd number:"))
# sum=num1+num2+num3
# print(sum)




# """Write a Python program that takes two numbers as input
#  from the user and performs arithmetic operations
# (addition, subtraction, multiplication, division, and modulus)
#  on them. Display the results of each operation."""
# num1=int(input("Enter a number:"))
# num2=int(input("Enter 2nd number:"))
# print(f"{num1}+{num2}={num1+num2}")
# print(f"{num1}-{num2}={num1-num2}")
# print(f"{num1}*{num2}={num1*num2}")
# print(f"{num1}/{num2}={num1/num2}")
# print(f"{num1}%{num2}={num2%num2}")




# """Create a Python program that prompts the user to enter 
# two numbers.Compare the numbers using comparison
#  operators (>, <, ==, !=, >=, <=) 
#  and print out the result of each comparison."""

# num1=int(input("Enter a number:"))
# num2=int(input("Enter 2nd number:"))
# print(f"{num1}>{num2} is {num1>num2}")
# print(f"{num1}<{num2} is {num1<num2}")
# print(f"{num1}=={num2} is {num1==num2}")
# print(f"{num1}!={num2} is {num1!=num2}")
# print(f"{num1}>={num2} is {num1>=num2}")
# print(f"{num1}<={num2} is {num1<=num2}")



# """Create a Python program that prompts the user to enter 
# their age and checks if they are eligible to vote. 
# Use logical operators to check if the age is greater 
# than or equal to 18 and less than or equal to 120. 
# Print a message indicating whether the person can 
# vote or not. """
# age=int(input("Enter your age:"))
# if age>=18 and age<=120:
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")



# """Write a program that takes inputs  from user 
# and prints the multiplication table of that number"""

# num=int(input("Enter a number:"))
# for i in range(1,11):
#     print(f"{i}*{num}={i*num}")





# """Write a function to calculate the factorial of a number 
# recursively. """

def fact():
    while True:
        num=int(input("enter a number:"))
        count=1
        for i in range(1,num+1):
            count=count*i
        print(f"factorial of {num} ={count}")
fact()



# #    2  Write a Python program to find all the valid identifiers in a given string. Assume that identifiers are separated by spaces.

# # text=input("enter a string:")
# # result=text.split(" ")
# # print(result)


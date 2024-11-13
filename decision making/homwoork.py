# 1

# name=input("Enter your first name:")
# print(f"Hello {name}")


#2


# name=input("Enter your first name:")
# name1=input("Enter your sure name:")
# print(f"Hello {name} {name1} ")

#3

# print("what do you call a bear with no teeth?\nA gummy bear.....!")


#4 


# a=int(input("Enter first number:"))
# b=int(input("Enter second number:"))
# y=a+b
# print(f"The total is {y}")


#5

# a=int(input("Enter first number:"))
# b=int(input("Enter second number:"))
# c=int(input("Enter therd number:"))
# y=(a+b)*c
# print(f"The answer is {y}")

#6 


# a=int(input("How many slices of pizza you started with..?"))
# b=int(input("How many slices you have eaten..?"))
# y=a-b
# print(f"you have only {y} slices of pizza left")



#7

# name=input("Enter your name:")
# age=int(input("Enter your age:"))
# new_age=age+1
# print(f"{name} next birthday you will be {new_age}")


#8


# total=int(input("Enter the total amount of bill:"))
# diners=int(input("how many diners are there:"))
# y=total/diners
# print(f"Each person want to give {y} rupees")


#9

# day=int(input("Enter  numbr of days:"))
# print(f"there are {day*24} hours, {day*24*60} minutes  and {day*24*60*60} seconds in {day} days")


#10 kg to pounds

# kg=int(input("Enter weight in kilogram:"))
# print(f"{kg}kg={kg*2204}")

#11 

# a=int(input("Enter a number over 100:"))
# if a>=100:
#     b=int(input("Enter a number under 10:"))
#     if b<=10 and b>0:
#         y=a//b
#         print(f"{b} will goes {y} times into {a}")
#     else:
#         print("invalid input")
# else:
#     print("Invalid input")
    

#12


# a=int(input("Enter a number:"))
# b=int(input("Enter second number:"))
# if a>b:
#     print(f"{b} {a}")
# else:
#     print(f"{a} {b}")


#13

# a=int(input("Enter a number under 20:"))
# if a>=20:
#     print("too high")
# else:
#     print("Thank you")



#14

# a=int(input("Enter a number between 10 and 20:"))
# if a>=10 and a<=20:
#     print("Thank you")
# else:
#     print("incorrect")



#15


# clr=input("enter your favourite colour:").strip().lower()
# if clr=="red":
#     print("I like red too")
# else:
#     print(f"i dont like {clr},I prefer red")




#16

# answer1=input("is it raining ..?  ").strip().lower()
# if answer1=="yes":
#     answer2=input("is it windy...?  ")
#     if answer2=="yes":
#         answer3=input("is it too windy for an umbrella")
#         if answer3=="yes":
#             print("plese attand class online")
#         elif answer3=="no":
#             print("take an umbrella")
#         else:
#             print("Incorrect input")
#     elif answer2=="no":
#         print("please get an umbrella")    
#     else:
#         print("Incorrect input")
# elif answer1=="no":
#     print("Enjoy your day")
# else:
#     print("Incorrect input")


#17

# age=int(input("how old are you:"))
# if age>=18:
#     print("you can vote")
# elif age==17:
#     print("you can learn to drive")
# elif age==16:
#     print("you can buy a lottery ticket")
# elif age<16:
#     print("you can go Trick or treacting")
# else:
#     print("invalid")


#18



# number=int(input("Enter a number:"))
# if number<10:
#     print("Too low")
# elif number>=10 and number<=20:
#     print("Correct")
# else:
#     print("Too high")




#19


# a=int(input("choose a number 1-3:"))
# if a==1:
#     print("Thank you")
# elif a==2:
#     print("Well done")
# elif a==3:
#     print("Correct")
# else:
#     print("Error message")




# price=int(input("Enter bike price:"))
# if price>100000:
#     tax=(price*15)/100
#     print(f"tax={tax}")
# elif price>=50000 and price<=100000:
#     tax=(price*10)/100
#     print(f"tax={tax}")
# elif price<50000:
#     tax=(price*5)/100
#     print(f"tax={tax}")

    



# total=0
# while(total<=50):
#     number=int(input("Enter a number:"))
#     total=total+number
# print(f"The total is...{total}")


# number=int(input("enter a number between 10 and 20:"))
# while(number<10 or number>20):
#     if number<10:
#         print("too low")
#     elif number>20:
#         print("too high")
#     number=int(input("enter a number between 10 and 20:"))
# if number>=10 or number<=20:
#     print("Thank you")




#Define a function named multiply that takes two parameters and returns their product. 
# Call this function with the arguments 4 and 5, and print the result.


# def pro(n1,n2):
#     print(n1*n2)


# pro(4,5)
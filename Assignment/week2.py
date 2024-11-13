"""Write program to check a number is even or odd
"""

# number=int(input("Enter a number:"))
# if number%2==0:
#     print(f"{number} is even")
# else:
#     print(f"{number} is odd")


"""Write a program to find greatest number among three numbers

"""


# num1=int(input("Enter a number:"))
# num2=int(input("Enter 2nd number:"))
# num3=int(input("Enter 3rd number:"))
# if(num1>num2) and (num1>num3):
#     print(f"{num1} is the greatest number")
# elif (num2>num1) and (num2>num3):
#     print(f"{num2} is the greatest number")
# else:
#     print(f"{num3} is greatest")




"""A shop will give discount of 10% if the cost of
 purchased quantity is more than 1000.
Ask user for quantity
Suppose, one unit will cost 100.
Judge and print total cost for user.

"""


# quantity=int(input("Enter the number of items:"))
# if quantity>=10:
#     # discont=(quantity*100)*(10/100)
#     total_cost=((quantity*100)-(quantity*100)*(10/100))
#     print(f"Total cost={total_cost}")
# else:
#     print(f"Total cost is {quantity*100} ")





"""Q6. Accept three sides of a triangle and check 
whether it is an equilateral, isosceles or scalene triangle.
Note :
An equilateral triangle is a triangle in which all three sides are equal.
A scalene triangle is a triangle that has three unequal sides.
An isosceles triangle is a triangle with (at least) two equal sides."""


# side1=int(input("Enter a side of triangle:"))
# side2=int(input("Enter 2nd side of triangle:"))
# side3=int(input("Enter 3rd side of triangle:"))
# if side1==side2==side3:
#     print("it is an Equalator trangle")
# elif side1!=side2!=side3:
#     print("it is a scalene Triangle")
# elif side1==side2 or side1==side3 or side2==side3:
#     print("it is an isosceles trangle")





"""Write a program to accept two numbers and 
mathematical operators and perform operation accordingly.
Like:
Enter First Number: 7
Enter Second Number: 99
Enter operator: +
Your Answer is : 16"""


# num1=int(input("Enter a number:"))
# num2=int(input("Enter 2nd number:"))
# oper=input("select your operator:")
# if oper=="+":
#     print(f"yor answer is : {num1+num2}")
# elif oper=="-":
#     print(f"yor answer is : {num1-num2}")
# elif oper=="*":
#     print(f"yor answer is : {num1*num2}")
# elif oper=="/":
#     print(f"yor answer is : {num1/num2}")



"""A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
Ask user to enter marks and print the corresponding grade.
"""


# mark=int(input("Enter your mark:"))
# if 80<=mark<=100:
#     print("yor grade is A")
# elif 60<=mark<80:
#     print("yor grade is B")
# elif 50<=mark<60:
#     print("yor grade is C")
# elif 45<=mark<50:
#     print("yor grade is D")
# elif 25<=mark<45:
#     print("yor grade is E")
# elif 0<=mark<25:
#     print("Failed")
# else:
#     print("Invalid mark")



"""Take values of length and breadth of a rectangle 
from user and check if it is square or not"""


# length=int(input("Enter length:"))
# breadth=int(input("Enter breadth:"))
# if length==breadth:
#     print("it is a square")
# else:
#     print("it is not a square")




"""Accept the age, sex ('M', 'F'), number of days 
and display the wages accordingly
Age                Sex             Wage/day
>=18 and <30        M                700
                    F                750
>=30 and <=40       M                800
                    F                850"""



# age=int(input("Enter your age:"))
# sex=input("Enter your Genter  M/F:").lower()
# days=int(input("Enter the number of age that you work:"))
# if 18<=age<30:
#     if sex=="m":
#         print(f"your salary={700*days}")
#     elif sex=="f":
#         print(f"your salary={750*days}")
# elif 30<=age<=40:
#     if sex=="m":
#         print(f"your salary={800*days}")
#     elif sex=="f":
#         print(f"your salary={850*days}")
# else:
#     print("error")






"""Write a program to check whether given 
year is leap year or not"""
# year=int(input("Enter the year:"))
# if (year%4==0 and year%100!=0) or year%400==0:
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not leap year")






"""Accept any city from the user and display monument of that city.
City.       Monument
Delhi       Red Fort
Agra        Taj Mahal
Jaipur      Jal Mahal"""

 
monuments={"delhi":"Red Fort","agra":"Taj Mahal","jaipur":"Jal Mahal"}
city=input("Emter city:").lower()
if city=="delhi":
    print(f"the moment of {city} is {monuments["delhi"]}")
elif city=="agra":
    print(f"the moment of {city} is {monuments["agra"]}")
elif city=="jaipur":
    print(f"the moment of {city} is {monuments["jaipur"]}")


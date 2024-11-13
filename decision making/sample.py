# a=int(input("Enter a number:"))
# if a==0:
#    print(f"{a} is neither  possitive or negative")
# elif a>0:
#     print(f"{a} is possitive")
# else:
#     print(f"{a} is negative")



#odd or even
# a=int(input("Enter a number:"))
# if a%2==1:
#     print(f"{a} is odd")
# else:
#     print(f"{a} is even")



# largest of three
# a=int(input("1st number:"))
# b=int(input("2nd number:"))
# c=int(input("3rd number:"))
# if (a>b and a>c):
#     print(f"Largest number is={a}")
# elif (b>a and b>c):
#     print(f"Largest number is={b}")
# else: 
#     print(f"Largest number is={c}")




#Examinasions
# a=int(input("Enter yor marks:"))
# if a>=90 and a<=100:
#     print("Your grade is A")
# elif a>=80 and a<=89:
#     print("Your grade is B")    
# elif a>=70 and a<=79:
#     print("Your grade is C")
# elif a>=60 and a<=69:
#     print("Your grade is D")    
# elif a>=50 and a<=59:
#     print("Your grade is E")
# elif a<50:
#     print("Failed.....!! ")      
# else:
#     print("Invalid")  




#bank balance
# bank_balance=int(input("Enter Bank balance:"))
# withdrawal=int(input("withdrawal amount:"))
# if withdrawal>=0 and withdrawal<bank_balance:
#     new_balance=bank_balance-withdrawal
#     if new_balance>500:
#        print("transaction successfull")
#        balance=bank_balance-withdrawal
#        print(f"Your available balance={balance}")
#     elif new_balance<=500:
#         print("Keep minimum balance")
# elif withdrawal>bank_balance:
#     print("Insufficient balance")
# else:
#     print("Invalid Amount")



# print("If it is raining...?   yes/no")
# answer=input()
# if answer=="yes":
#     print("is it windy...?   yes/no")
#     answer2=input()
#     if answer2=="yes":
#         print("it is too windy for an umbrella..?   yes/no")
      
#     elif answer2=="no":
#             print("Please take an umberlla U")
#     else:
#          print("Get out")
# elif answer=="no":
#      print("Enjoy the day")
# else:
#      print("get out")
            
          
    
# num1=int(input("Enter a number:"))
# num2=int(input("Enter second number:"))
# operator=input("Enter an operator:")
# if operator=="+":
#     result=num1+num2
#     print(f"result of {num1} + {num2} = {result}")    
# elif operator=="-":
#     if num1>num2:
#         result=num1-num2
#         print(f"result of {num1} - {num2} = {result}")
#     elif num2>num1:
#         result=num2-num1
#         print(f"result of {num1} - {num2} = {result}")        
# elif operator=="*":
#     result=num1*num2
#     print(f"result of {num1} * {num2} = {result}")
# elif operator=="/":
#     if num2!=0:
#         result=num1/num2
#         print(f"result of {num1} / {num2} = {result}")
#     elif num2==0:
#         print("not defined")
# else:
#     print("Invalid operator")









# num=10
# result="positive" if num>0 else "negative" #terrinary operator
# print(result)

#variable="return value" if(condition) else "return value"


# a=int(input("Enter a number"))
# result="odd" if a%2==0 else "even"
# print(result)


# a=int(input("Enter first number:"))
# b=int(input("Enter first number:"))
# result= f"{a} is largest" if a>b else  f"{b} is largest "
# print(result)


#--------------------------------------------------------------------------------------------------





# i=1

# while(i<=5):

#     print("Hello")
    
#     i=i+1



# num=int(input("Enter a number:"))
# temp=num
# reverce=0
# while(temp>0):
#     digit=temp%10
#     reverce=reverce * 10 + digit
#     temp=temp//10
# if num==reverce:
#     print("palindrom")
# else:
#     print("not")


num=int(input("Enter a number:"))
ord=len(str(num))
temp=num
sum=0
while(temp>0):
    digit=temp%10
    sum=sum+digit*ord
    temp=temp//10
if num==sum:
    print("armstrome")
else:
    print("not")
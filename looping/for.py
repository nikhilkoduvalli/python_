# name=input("Enter your name:")
# for i in range(0,3):
#     print(name)


# name=input("Enter your name:")
# i=0
# while(i<=3):
#     print(name)
#     i=i+1

# for i in range (10,1,-3):
#     print(i)

# for i in range (1,10,3):
#     print(i)




# name=input("Enter your name:")
# num=int(input("enter a number:"))
# for i in range(num):
#     print(name)














# visitors=int(input("How many people you want to invite?:"))
# if visitors<10:
#     for i in range (visitors):
#         name=input("Enter the names:")
#         print(f"{name} are invited")
# else:
#     print("Too many people")







# number=int(input("Enter a number:"))
# if number<2:
#     print("Get out")
# else:
#     for i in range(2,number):
#         if number%i==0:
#             print("Not a prime")
#             break
#     else:
#         print("prime")





# total=0
# for i in range (5):
#         num=int(input("Enter a number:"))
#         total=total+num
#         qust=input("do you want to include?...yes/no:").lower()
#         if qust!="yes":
#                break           
# print(f"total={total}")




# total=0
# for i in range(5):
#     num=int(input("Enter a number:"))
#     print("do you want to include the numbers")
#     answer=input (": ")
#     if answer=="yes":
#         total=total+num
#     elif answer=="no":
#         break
# print (total)




# total=0
# for i in range(5):
#     num=int(input("Enter a number:"))
#     quest=input("do you want to include the numbers")
#     if quest=="y":
#         total+=num
#     else:
#           break
# print(total)

    


# # question 043


# direction=(input ("in which direction do you want to count : ")) 
# if direction=="up":
#     top=int(input("what is the top number : ")) 
#     for i in range (1, top+1):
#          print (i)
# elif direction=="down":
#     num=int (input("enter a number below 20 : ")) 
#     for i in range(20, (num-1), -1):
#          print(i)
# else:
#     print("puriyale thambi")



 
# palindrom



# number=int(input("Enter a number:"))
# temp=number
# reverse=0
# while(temp>0):
#   digit= temp % 10
#   reverse=reverse * 10 + digit
#   temp=temp//10
# if number==reverse:
#        print(f"{number} is palindrome")
# else:
#        print(f"{number} is not palindrome")




# number=int(input("Enter a number:"))
# # temp=number
# reverse=0
# while(number>0):
#     digit=number%10                                #modulus 
#     reverse=reverse*10+digit                       
#     number=number//10
# print(reverse)




# course=input("Enter a name:").lower()
# count=0
# for i in course:
#     if i in "aeiou":
#         print(i)
#         count=count+1
# print(f"no of vowels in the word={count}")


# course=input("Enter a name:").lower()
# count=0
# count2=0
# for i in course:
#     if i in "aeiou":
#       #   print(i)
#         count=count+1
#     else:
#         count2=count2+1
# print(f"no of vowels in the word={count}")
# print(f"no of consonants in the word={count2}")



  #################################################






#continue



# for i in range(6):
#     if i==3:
#         continue
#     print(i)



# num=int(input("enter a number:")) 
# ord=len(str(num))
# temp=num
# sum=0
# while(temp>0):
#     digit=temp%10
#     sum=sum + digit**ord
#     temp=temp//10
# if sum==num:
#     print(f"{num}is an armstrom")
# else:
#     print(f"{num} is not an armstrom")





########################################################
 #factorial


# num=int(input("Enter a number:"))
# fact=1
# if num==0:
#     print("factorial of 0 is 1")
# elif num<0:
#     print("Invalid input")

# elif num>0:
#   for i in range(1,num+1):
#     fact=fact*i
#   print(f"factorial of {num}={fact}") #1234



# row=int(input("Enter a number:"))
# for i in range (5):
#     for j in range(i+1):
#         print("*",end=" ")
#     print("\n")



# row=int(input("Enter a number:"))
# for i in range (5):
#     for j in range(i+1):
#         print(j+1,end=" ")
#     print("\n")



# number=int(input("Enter a number:"))
# temp=number
# reverse=0
# while(temp>0):
#      digit=temp % 10
#      reverse=reverse * 10 + digit
#      temp=temp // 10
# if number==reverse:
#      print(f"{number} is a palindrome")
# else:
#      print(f"{number} is not a palindrome")




# number=int(input("Enter a number:"))
# temp=number
# reverse=0
# while(temp>0):
#   digit= temp % 10
#   reverse=reverse * 10 + digit
#   temp=temp//10
# if number==reverse:
#        print(f"{number} is palindrome")
# else:
#        print(f"{number} is not palindrome")



# name=input("Enter a name:")
# number=int(input("Enter a number:"))
# if number<10:
#     for i in range(1,number+1):
#         print(f"{name}")
# elif number>10:
#     for i in range(3):
#         print("Too high")






# people=int(input("How many people you want to invite:"))
# if people<10:
#     name=input("Enter their names:")
#     for i in range(people-1):
#         print(f"{name} was invited")
#         name=input("Enter their names:")
# elif people>=10:
#     print("Too many people")
        



# total=0
# # number=int(input("Enter a number:"))
# for i in range(5):
#     number=int(input("Enter a number:"))
#     quest=input("Do you want to include this number yes/no? ").lower()
#     if quest=="yes":
#         total=total+number
#     elif quest=="no":
#         total=total
# print(f"total is {total}")
    



# quest=input("Which direction do you want to count  up/down:").lower()
# if quest=="up":
#     topnum=int(input("Enter to number:"))
#     for i in range(1,topnum+1):
#         print(i)
# elif quest=="down":
#     num=int(input("Enter a number below 20:"))
#     if num<20:
#         for i in range(20,num-1,-1):
#             print(i)
#     elif num>=20:
#         print("get out")
#





#prime


# num=int(input("Enter a number:"))
# if num<2:
#     print("get out")
# else:
#     for i in range(2,num):
#         if num%i==0:
#             print("not a prime:")
#             break
#     else:
#         print("is prime")




#palindrome


# number=int(input("Enter a number;"))
# temp=number
# reverse=0
# while(temp>0):
#     digit=temp%10
#     reverse=reverse*10+digit
#     temp=temp//10
# if reverse==number:
#     print("is palindrome")
# else:
#     print("not")


#amstrome number


# number=int(input("Enter a number:"))
# ord=len(str(number))
# temp=number
# sum=0
# while(temp>0):
#     digit=temp%10
#     sum=sum+digit**ord
#     temp=temp//10
# if number==sum:
#     print("is amstrong")
# else:
#     print("not")
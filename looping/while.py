# i=1

# while(i<=5):

#     print("Hello")
    
#     i=i+1


############################

#print 1-10

# i=1
# while(i<=10):
#     print(i)
#     i=i+1




############################


# i=10
# while(i>=1):
#     print(i)
#     i=i-1



############################


# number=int(input("Enter a number:"))
# total=0
# while(number!=0):
#     total=total+number
#     number=int(input("Enter a number:"))
# print(total)


############################


# i=1
# while(i<=50):
#     if i%2==0:
#         print(i)
#     i=i+1



############################


# total=0
# while(total<=50):
#     num=int(input("Enter a number:"))
#     total=total+num
#     print(f"the total is{total}")



# a=int(input("Enter a value between 10-20:")) 
# while(a<10 or a>20):
#     if a<10:
#         print("Too low")   
#     elif a>20:
#         print("Too high")
#     a=int(input("try again"))
# print("thank you")

####################################33
#1

# i=1
# total=0
# while(i<=100):
#     total=total+i
#     i=i+1
# print(f"sum of 1-100{total}")


#####################################
#2



# i=1
# total=0
# while(i<=50):
#     if i%2==0:
#         total=total+i
#     i=i+1
# print(total)



##################################
#3


# i=1
# total=0
# while(i<=99):
#     # if i%2==1:
#     total=total+i
#     i=i+2
# print(total)


###################################
#4




# i=99
# while(i>=1):
#     if i%2==1:
#         print(i)
#     i=i-1



######################################
#5



# a=int(input("Enter a number:"))
# while(a<=5):
#     a=int(input("Enter a number:"))
# print(f"The last number entered {a}")





########################################
#6



# a=int(input("Enter a number:"))
# b=int(input("Enter another number:"))
# total=a+b
# quest=input("do you want to add another number..?  y/n  :").lower()
# while(quest=="y"):
#     c=int(input("Enter another number:"))
#     total+=c
#     quest=input("do you want to add another number..?   :")
# print(total)




# i=1800
# while(i<=2024):
#     if i%100==0:
#         print(f"{i}is a centery year")
#     i=i+1



# i=1800
# while(i<=2024):
#     if (i%4==0 and i%100!=100) or (i%400==0):
#         print(f"{i}is a leap year")
#     i=i+1







# a=50
# n=int(input("Enter a number:"))
# count=1
# while(n!=50):
#     if n<50:
#         print("Your answer is too low")
#     elif n>50:
#         print("Your answer is too high")
#     n=int(input("Try again:"))
#     count=count+1
# print(f"well done you enerd{a} at count {count}")

    



n=int(input())
arr=list(map(int, input().split()))

unorderd=list(set(arr))
unorderd.sort()
print(unorderd[-2])
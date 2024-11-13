# a=int(input("Enter a number:"))
# if a>=1 and a<=100:
#     if a%2==1:
#         print("Weird")
#     elif a%2==0:
#         if a>=2 and a<=5:
#             print(" Not Weird")
#         elif a>=6 and a<=20: 
#             print("Weird")
#         elif a>20:
#             print("Not weird")



    

    #---------------------------------------------------------------------------------------------------------

# n = int(input("Enter limit:"))
# if n>=1:
#     i=1
#     while(i<=n):
#         print(i**2)
#         i=i+1
# else:
#     print("Error")



#leep yer


# a=int(input("Enter an year:"))
# if a%4==0:
#     print("True")
# elif a%400==0:
#     print("True")
# elif a%100==0:
#     print("Falls")





# n=int(input())
# for i in range(1,n+1):
#     print(i,end="")

    


# numbers=[]
# limit=int(input())
# if 2<=limit<=10:
#     for i in range(limit):
#         ranks=int(input())
#         numbers.append(ranks)

# largest_num=0
# second_largest=0
# for i in numbers:
#     if i>second_largest and i>largest_num:           
#         second_largest=largest_num                   
#         largest_num=i                                
#     elif i>second_largest and i<largest_num:
#         second_largest=i
# print(second_largest)









# N = []
# limit = int(input("Enter a limit: "))

# while True:
#     opp = int(input("Select your operation:\n1. Insert\n2. Print\n3. Remove\n4. Append\n5. Sort\n6. Pop\n7. Reverse\n0. Exit\n"))

#     if opp == 0:
#         break

#     if opp == 1:
#         ins = int(input("Enter the number to insert: "))
#         N.append(ins)
#     elif opp == 2:
#         print("Current list:", N)
#     elif opp == 3:
#         remo = int(input("Enter the number to remove: "))
#         if remo in N:
#             N.remove(remo)
#         else:
#             print("Number not found in list.")
#     elif opp == 4:
#         poss = int(input("Enter the index to append after: "))
#         num = int(input("Enter the number to append: "))
#         N.insert(poss + 1, num)
#     elif opp == 5:
#         N.sort()
#         print("List sorted.")
#     elif opp == 6:
#         if len(N) > 0:
#             popped = N.pop()
#             print("Popped element:", popped)
#         else:
#             print("List is empty, cannot pop.")
#     elif opp == 7:
#         N.reverse()
#         print("List reversed.")
#     else:
#         print("Invalid operation selected.")

# print("Final list:", N)




# x = int(input().strip())
# y = int(input().strip())
# z = int(input().strip())
# n = int(input().strip())

# coordinates = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1)]

# filtered_coordinates = [coord for coord in coordinates if sum(coord) != n]

# print(filtered_coordinates)


mark=0
count=0
limit=int(input("Enter the number of students to be added:"))





# places=["knr","tvm","ekm"]   #data type in python ,containing varsatile collection of items str,int,boolian
# print(places)

# places.append("plkd")    # add an element to the end of the list
# print(places)

# print(places.count("knr"))   #returns count of elements in a list

# places.insert(1,"bnglr")     # add items into the list in the specific index posision
# print(places)


# print(places[0:2])     #print 0-2 position element from the list as list


# print(places[1])        #pic a perticular item from a list


# print(places)


#numbers.pop()            to pop the last index value

#numbers.pop(10)            to pop the last index value 10


#numbers.extend()            to add a list of elements into a list


#numbers.reverce()            to revers the given list

#numbers.remove()            to remove a spesific item


# numbers=[1,2,3,4,5,6,7,8]
# for i in numbers:
#     print(i)
#     print(i**2)




# numbers=[1,2,3,4,5,6,7,8]
# even_list=[]
# odd_list=[]
# for i in numbers:
#     if i%2==0:
#         even_list.append(i)
        
#     else:
#         odd_list.append(i)
# print(f"list of even numbers={even_list}")
# print(f"list of odd numbers={even_list}")







# numbers=[3,8,2,6,7,9]
# smallest_num=numbers[0]
# for i in numbers:
#     if i<smallest_num:
#         smallest_num=i
# print(f"{smallest_num}")






# numbers=[3,8,2,6,7,9]
# largest_num=numbers[0]
# second_largest=[1]
# for i in numbers:
#     if i>largest_num:
#         largest_num=i
#     elif i<largest_num and i==second_largest:
#         second_largest=i
# # print(f"{second_largest}")
# print(f"{largest_num}")
# print(f"{second_largest}")




# numbers=[3,2,5,8,6,9,10]
# largest_num=numbers[0]
# second_largest=numbers[1]
# for i in numbers:
#     if i>second_largest and i>largest_num:
#         second_largest=largest_num
#         largest_num=i
# print(f"{second_largest}")



#wap to find unique elements and their count



# numbers=[1,3,6,2,7,3,5,6]
# count=0
# list=[]
# list2=[]
# for i in list:
#     if i not in list:
#         list.append(i)
#     else:
#         count=count+1
#         list2.append(i)
# print(f"multiple numbers={list2}")
# print(f"count={count}")




#wap to find the count of odd numbers and even numbers 


# numbers=[1,2,3,4,5,6,7,8]
# odd_list=[]
# even_list=[]
# count=0
# count1=0
# for i in numbers:
#     if i%2==1:
#         odd_list.append(i)
#         count=count+1
#     else:
#         even_list.append(i)
#         count1=count1+1
# print(f"no of odd numbers in the list={count}")
# print(f"no of even nimbers in the list={count1}")






# numbers=[1,2,3,4,5,6,7,8]
# sum=0
# for i in numbers:
#     if i%2==1:
#         sum=sum+i
# print(sum)





# names=("knr","plkd","kollm","tvd")
# place=input("Enter a place:")
# ans=names.index(place)
# print(ans)
# number=int(input("Enter a numbe:"))
# ans2=names[number]
# print(ans2)

 



# numbers=[1,2,[10,20,[300,400,500],50,60],4,5]
# # print(numbers[2])
# # print(numbers[2][2])
# ans=numbers[2][2]
# new_list=list(ans)
# new_list.append(600)
# ans=tuple(new_list)
# numbers[2][2]=ans
# print(numbers)



numbers=[3,8,2,6,7,9]
new_list=[i for i in numbers if i%2==0]
print(sorted(new_list))

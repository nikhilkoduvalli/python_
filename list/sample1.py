# numbers=[11,3,2,9,8,10]
# largest_num=0
# second_largest=0
# for i in numbers:
#     if i>second_largest and i>largest_num:           
#         second_largest=largest_num                   
#         largest_num=i                                
#     elif i>second_largest and i<largest_num:
#         second_largest=i
# print(second_largest)




# numbers=[3,4,1,3,5,2,1,10]                             
# numbers.sort()
# smallest=numbers[0]
# second_smallest=numbers[-1]
# for i in numbers:
#     if i<second_smallest and i<smallest:
#         second_smallest=smallest
#         smallest=i
#     elif i<second_smallest and i>smallest:
#         second_smallest=i
# print(second_smallest)








# places=["kochi","kollam","tvm","chennai"]
# new_list=[]
# for i in places:
#     if "c" in i:
#         new_list.append(i)
# print(new_list)




# places=["kochi","kollam","tvm","chennai"]
# new_list=[]
# for i in places:
#     for j in i:
#         if j=="c":
#             new_list.append(i)
# print(new_list)



#        #list compreprehension

# places=["kochi","kollam","tvm","chennai"]       #i=element to be added to the new list  
# new_list=[i for i in places if "c" in i]
# print(new_list)


# numbers=[1,2,3,4,5]
# new_list=[i**2 for i in numbers]
# print(new_list)



# new_list=[i for i in range(11) if i%2==0]
# print(new_list)



       #wap to print numbers from 1 to 1000 that is divisible by 7
# div_7=[i for i in range(1,1001) if i%7==0]
# print(div_7)


# even=[i for i in range(1001) if i%2==0]
# print(even)


      #wap  to print nukmbers from 1-1000 which has 3


# new_list=[i for i in range(1,1001) if "3" in str(i)]                 # comprwehention methode
# print(new_list)



# new_list=["Even" if i%2==0 else "odd" for i in range(1,101)]     #first new_list add cheyyandath pinna conditions
# print(new_list)




      #wap to find the numbers from 1-1000 tha is divisible by 3 and 5


# new_list=[i for i in range(1,1001) if i%3==0 and i%5==0]
# print(new_list)


      #perint a new list that have common in th given two list 

# list1=[1,2,3,4]
# list2=[1,3,5]
# new_list=[i for i in list1 if i in list2]
# print(new_list)






#wap to print only the numbers in  the sentence "in 1984 there where 13 instances of a protest with over 1000 people attending"



# setence="in 1984 there where 13 instances of a protest with over 1000 people attending"
# words=setence.split()
# new_list=[i for i in words if i.isdigit()]
# print(new_list)


   #get 4 digit words from the sentence "on a summer day somner smith went went simming in the sun an his red skin stunk"

# setence="on a summer day somner smith went went simming in the sun an his red skin stunk"
# words=setence.split()
# for i in words:
#     if len(i)<4: 
#         print([i],end=" ")
# # new_list=[i for i in words if len(i)<4]
# # print(new_list)







# name={1,2,3}
# name2={3,4,5}
# new_list=name.difference(name2)
# print(new_list)





# list1=[1,2,4,1,2,3,5]
# new=set(list1)
# s=list(new)  
# print(s)



# list1 = [1, 2, -1, 1, 2, 5, 1]
# list2 = []
# for i in list1:
#     if i not in list2:  
#         list2.append(i)
# list2.sort()
# print(list2)











# s=set()
# s.add(2)
# print(s)





# student={"name":"nikhil","id":12}

 

# student["name"] ="usman"
# print(student)


# print(student.keys()) 


# student.pop("name")
# print(student)






# print(student.items())        #dict_items([('name', 'nikhil'), ('id', 12)]) return all the pairs as a tuple in alist




# for i in student:
#     print(f"{i}={student[i]}")

        #wap to ud\pdate place=kochi



student={"name":"nikhil","id":12,"place":"knr"}
for i in student:
    if i =="plase":
        student[i]="kochi"
    print(f"{i}={student[i]}")
    




# dic1={"name":"appu","age":17}
# dict2={"place":"knr","state":"kerala"}

# dic1.update(dict2)


# print(dic1)







# keys=["ten","twenty","thirty"]
# values=[10,20,30]
# dict={}
# for i in keys:
#       for j in values:
#       dict[keys[i]=values]





#         remove salary and location from the list


# dic={"name":"hari","salary":12000,"location":"kochi","position":"trainer"}
# remove_item=["salary","location"]
# for i in remove_item:
#     if i in dic:
#         dic.pop(i)
# print(dic)




#        convert the two list in to a single dictionary  keys=["ten","twenty","thirty"] values=[10,20,30]





# keys=["ten","twenty","thirty"]
# values=[10,20,30]
# dic={}
# for i in range(len(keys)):
#     dic.update({keys[i]:values[i]})
# print(dic)




# tv_show=["chottabeeem","ben 10","Oogy and Cocroch","Motu patlu"]
# for i in tv_show:
#     print(i)
# fifth=input("Enter another show:")
# pos=int(input("Enter the possition  u want to insert:"))
# tv_show.insert(pos-1,fifth)
# for i in tv_show:
#     print(i)





# nums=[]
# while True:
#     number=int(input("Enter a number:"))
#     nums.append(number)
#     print(nums)
#     if len(nums)>=3:
#         quest=input("Do you want to input the number yes/no  :").lower()
#         if quest=="yes":
#             continue
#         elif quest=="no":
#             nums.pop()
#         else:
#             break

#wap to cheque the given 2 arguments if they are even return lesser ,if odd return max


# def odd_even(num1,num2):
#     if num1%2==0 and num2%2==0:
#         return min(num1,num2)
#     elif num1%2==1 and num2%2==0:
#         return max(num1,num2)
    
# print(odd_even(2,6))



#given two integers ,if one of the two integer is 20 return True or the sum of the tow integers is 20 return True


# def twenty(num1,num2):
#     if num1==20 or num2==20 or num1+num2==20:
#         return True
#     else:
#         return False
# print(twenty(10,10))






# Given an integer n, return True if n is within 10 of either 100 or 200 
# alnost there(90) -→> True
# alnost_ there(104) --› True
# almost_there(150) --> Faise
# almost there (209) --› True


# def within100(num):
#     if 90<=num<=110 or 190<=num<=210:
#         return True
#     else:
#         return False
    
# print(within100(209))



# Given a list of ints return True if the list contains a 3 next to a 3 somewhere.
#has_33 ([1,3,3]) -> True 
# #has_33 ([1,3,1,31) -> False 
# #has_33 ([3,1,3]) -> False

# def cheque_adjacent(list):
#     for i in  range(0,len(list)-1):
#         if list[i]==3 and list[i+1]==3:
#             return True
#     else:
#         return False
        

# print(cheque_adjacent([3,1,3]))





# def sum_num(*args):
#     return sum(args)

# print(sum_num(1,2,3,4,5,6))






# def sum_num(*args):
#     sum=0
#     for i in args:
#         sum=sum+i
#     return sum

# print(sum_num(1,2,3,4,5,6))








#wap to filter even numbers from the list 



# def filter_evensq(list):
#     return [i**2 for i in list if i%2==0]

# print(filter_evensq([]))






#wap to create a function to filter even and odd numbers from the list

# def filter_odev(list):
#     return ["even" if i%2==0 else "odd" for i in list]


# print(filter_odev([1,2,3,4,5,6,7,8]))










#wap tocreate a funtion to filter even numbers from the list and write it to a file





# def write_file(path,numbers):
#     file=open(path,"w")
#     for i in numbers:
#         if i%2==0:
#             file.write(f"{str(i)} \n")
#     file.close()
#     return file


# write_file("sq4_numbers.txt",[1,2,3,4,5,6,7])





#wap to create a funtion to filter odd numbers from a list compute their squers ande write it to a file as a list

# def write_odd(path,numbers):
#     file=open(path,"w")
#     num=([i**2 for i in numbers if i%2==1])
#     file.write(str(num))
#     file.close()
#     return file

# write_odd("sq_num.txt",[1,2,3,4,5,6])




# def courses(name,cource,institution="luminar"):
#     print(f"{name}is attanding{cource} in {institution}")


# courses("Nikhil","Data Science")




""" wap to create functions addition, subtraction, divison, multiplication, modulus, floor
division
values,
# in these functions use decorators for avoiding getting negative and fractioned

"""

# def swap_num(func):
#     def wrap(a,b):
#         if a<b:
#             a,b=b,a
#         return func(a,b)
#     return wrap


# @swap_num
# def math_op(a,b):
#     print(f"Sum={a+b}")
#     print(f"difference={a-b}")
#     print(f"Product={a*b}")
#     print(f"Subtraction={a/b}")

# math_op(4,3)


"""# wap to add 1 to 100 to a list and filter the elements divisible by 3 or 6 and add
them to a new list,
# now create a function to check each if number is odd
return "num is odd" else
"num is even"""



# def odd_even(list1):
#     new_list2=["even" if i%2==0 else "odd" for i in list1]
#     return new_list2


# list1=[]
# for i in range(1,101):
#     list1.append(i)
# new_list=[i for i in list1 if i%3==0 or i%6==0]



# print(odd_even(new_list))














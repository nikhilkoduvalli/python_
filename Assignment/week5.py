"""Write a program that uses a for loop to print 
numbers from 1 to 10, but breaks the loop when the number is 5.

"""

for i in range(1,11):
    if i==5:
        break
    print(i)


"""Write a program that iterates over a list of 
integers and breaks the loop when a negative number is encountered.

"""

numbers=[1,2,3,-2,5,6,9]
for i in numbers:
    if i<0:
        break
    print(i)



"""Write a program that prints all even numbers 
from 1 to 10 using a While loop and continue statement"""

number = 1

while number <= 10:
    if number % 2 != 0:
        number=number+1  
        continue 
    
    print(number)
    
    number=number+1


"""Write a program that prints the sum of all 
positive numbers in a list using a for loop and continue statement.

"""

numbers=[1,2,3,4,-4,-7,-8,5,2,4,5]
sum=0
for i in numbers:
    if i<0:
        continue
    sum=sum+i
print(f"the sum of all possitive numbers in the list {sum}")



"""Write a simple program that includes a 
pass statement in a for loop."""


numbers = [1, 2, 3, 4, 5]

for i in numbers:
    if i == 3:
        pass 
    else:
        print(i) 


"""Write a Python function that uses break to exit 
early if a certain condition is met while iterating through a list.

"""

def exit(list1):
    for i in list1:
        if i<0:
            print(f"found a -ve number {i} so exiting the looop")
            break
        print(f"previous numbers {i}")
    
exit([1,2,3,-4,5,-1,-1,-2,3,4,5])


"""Write a program that uses continue to skip over certain iterations in a 
loop that processes a list of strings, skipping strings shorter than 3 characters.
strings = ["a", "abc", "defg", "hi", "jkl"]

"""



strings = ["a", "abc", "defg", "hi", "jkl"]
new_list=[]
for i in strings:
    if len(i)<3:
        continue
    new_list.append(i)
print(new_list)


"""Write a Python function that processes a list of numbers, 
using continue to skip processing for numbers less than 5.

"""

def less_5(list1):
    for i in list1:
        if i<5:
            continue
        print(i)
less_5([1,2,3,4,5,6,7,8,9,0])



"""Write a program that uses break and continue in a nested 
loop to find and print the first pair of numbers (i, j) where i * j is greater than 10.

"""


for i in range(1,10):
    for j in range(i):
        pro=i*j
        if pro<=10:
            continue
        print(f"first pair of numbers {(i,j)}")
        break

    else:
        continue
    break



"""Write a program that uses continue to skip over specific words in a list while printing the rest.
words = ["apple", "banana", "cherry", "date", "elderberry"]
skip_words = ["banana", "date"]

"""
  
words = ["apple", "banana", "cherry", "date", "elderberry"]
skip_words = ["banana", "date"]
for i in words:
    if i in skip_words:
        continue
    print(i)
    








""" Write a program to create a module name my_functions 
and perform string manipulation function for counting 
the vowels and reversing the string 
"""


def string_manipulation(string):
    count=0
    vowels="aeioqAEIOQ"
    for i in string:
        if i in vowels:
            count+=1
    print(f"number of vowels in the string is {count}")
    print(f"reverse of the string = {string[::-1]}")

string_manipulation("Nikhil")


# Week 4: Pattern using while and for loops.


"""1

* * * * *
* * * *
* * *
* *
*
"""
for i in range(5,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()






"""# 2

1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""
for i in range(5):
    for j in range(i+1):
        print(i+1,end=" ")
    print()







"""# 3
* * * *
* * *
* *
*
* *
* * *
* * * *
"""

for i in range(4,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(2,5):
    for j in range(i):
        print("*",end=" ")
    print()










"""# 4

         1
       1 2 1
     1 2 3 2 1
   1 2 3 4 3 2 1
"""



for i in range(1,5):
    for j in range(4-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    for j in range(i-1,0,-1):
        print(j,end=" ")
    print()








"""# 5


1
2 2
3 3 3
4 4 4 4
3 3 3
2 2
1
"""
for i in range(4):
    for j in range(i+1):
        print(i+1,end=" ")
    print()
for i in range(3,0,-1):
    for j in range(i):
        print(i,end=" ")
    print()








"""# 6

1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
"""

for i in range(1,6):
    for j in range(1,6):
        print(j,end=" ")
    print()









"""# 7

1 
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""
for i in range(5):
    for j in range(i+1):
        print(j+1,end=" ")
    print()






"""# 8

5 5 5 5 5
5 5 5 5
5 5 5
5 5
5
"""

for i in range(5,0,-1):
    for j in range(i):
        print(5,end=" ")
    print()







 
"""9

 0 1 2 3 4 5
 0 1 2 3 4
 0 1 2 3
 0 1 2
 0 1
"""




for i in range(6,1,-1):
    for j in range(i):
        print(j,end=" ")
    print()






"""10

1 
2    3
4    5     6
7    8     9   10
11   12    13  14   15"""



num=1
for i in range(5):
    for j in range(i+1):
        print(num,end=" ")
        num+=1
    print()






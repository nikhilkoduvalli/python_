 #read,  write,  appand
#  r ,    w,       a

# python file handling refers to the prosses of working with the files on the fole System
# it involves operation such as reading from file,writing.......
#file handling is an important part of any web application
#python has several functions for creating reading writing and updating the file


#file=open("file_name","mode")
#print(fil.read())

# file = open("file1.py","r")
# for data in file:
#     print(data)






#   write   W

# file = open("new1.txt","w")
# file.write("Welcome to file operation")
# file.close()



# file = open("new1.txt","w")
# file.write("Welcome mr ooomanakkuttan")
# file.close()




#wap to create a file named bio.text and add the details of name and course then open the same file and t\read the value



# file=open("bio.txt","w")
# file.write("NIKHIL \n")
# file.write("PYTHON DATA SCIENCE")
# file.close()

# fp=open("bio.txt")
# print(fp.readline())




#####################################################################################



#appand()    use to add a content inmto an existing file without removing any content 'a'


# file=open("bio.txt","a")
# file.write(" hi\n")
# file.close()




#wap to create a new file called name.txt and add youtr namre using input function


# file=open("name.txt","w")
# name=input("Enter your name:")
# file.write(name)
# file.close()

# file=open("name.txt","a")
# for i in range(3):
#     name2=input("Enter another name:")
#     file.write(name2)
# file.close()




 
# choice=int(input("1)create a new file  2)Display the content  3)Add a new item to the file"))
# if choice==1:
#     file=open("Subject.txt","w")
#     subject=input("Enter a subject:")
#     file.write(subject)
#     file.close()
# elif choice==2:
#     file=open("Subject.txt","r")
#     print(file.read())
#     file.close()
# elif choice==3:
#     file=open("Subject.txt","a")
#     sub2=input("Enter another subject:")
#     file.write(sub2)
#     file.close()
#     file=open("Subject.txt","r")
#     print(file.read())
#     # file.close()

# else:
#     print("Go to hell")




#create a new file into an existing folder 


# file=open("C:/Users/nikhi/OneDrive/Desktop/python/fileOPERATION/new.txt","w")
# file.write("Welcome")
# file.close()




# file=open("C:/Users/nikhi/OneDrive/Desktop/python/fileOPERATION/new.txt","w")
# names=[]
# for i in range(5):
#     name=input("Enter an item:")
#     names.append(name)
#     print(name)
#     for i in names:
#         print(f"{i}\n")





#wap to enter the prime numbers from 1 to 10 into a list then add each element into a file in itration



# file=open("C:/Users/nikhi/OneDrive/Desktop/python/fileOPERATION/primes.txt","w")
# primes=[]

# for i in range(1,11):    #i=1           #i=2            #i=3               i=4
#     if i==1:              #continue
#         continue
#     for j in range(2,i):                #range(2,2)     range(2,3)         range(2,4)
#         if i%j==0:
#             break
#     else:
#         primes.append(i)
        
# for i in primes:
#     file.write(f"{i}\n")
# file.close





#####################################################

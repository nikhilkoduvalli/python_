# class Student:
#     name=str

#     def __init__(self,name):
#         self.name=name
#     def name_(self):
#         print(self.name)
    
# obj1=Student(name="hari")
# obj2=Student(name="suni")
# obj2.name_()
# obj1.name_()



# class Emploiee:
#     name=str
#     place=str
#     position=str
#     def __init__(self,name,place,position):

#         self.name=name
#         self.place=place
#         self.position=position

#     def name_position(self):
#         print(f"name is {self.name} and position is {self.position}")

# obj1=Emploiee(name="nikhil",place="knr",position="data engineer")

# obj1.name_position()


class Bank:  
    bank_name="SBI"
    acc_number:int
    balance:int
    name:str

    def __init__(self,acc_number,balance,name):
        self.acc_number=acc_number
        self.balance=balance
        self.name=name
       

    def display(self):
        print(f"Welcome to {self.bank_name}")
        print(f" Acc_number {self.acc_number}")
        print(f" Balance: {self.balance}")
        print(f" Name: {self.name}")
    
    def deposit(self,amount):
        self.balance=self.balance+amount
        print(f"{amount} deposited succesfully.....!")
    

    def withdrawel(self,amount):
        if amount>self.balance:
            print(f"insufficiant balance....!")
        else:
            print(f"transaction Succesfull...!")
            print(f"{amount} is debited from your bank account{self.acc_number}")
            self.balance=self.balance-amount



obj1=Bank(acc_number=423,balance=100000,name="Nikhil k")


obj1.display()
obj1.deposit(1000)
obj1.display()
obj1.withdrawel(2000)
obj1.display()
 























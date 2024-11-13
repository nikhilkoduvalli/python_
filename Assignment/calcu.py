import calculator
def main():
    while True:
        print("\nAvailable operations:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")        
        choice = input("Enter your choice (1/2/3/4/5): ")
        if choice==5:
            print("Thank you for commong,By By...")
            break
        if choice not in(["1","2","3","4"]):
            print("Pleace enter a valid choice...")
            continue
        try:
            num1=int(input("Enter first number:"))
            num2=int(input("Enter 2nd number"))
            if choice=="1":
                result=calculator.add(num1,num2)
                print(f"The sum of the numbers = {result}")
            elif choice=="2":
                result=calculator.difference(num1,num2)
                print(f"The difference of the numbers = {result}")
            elif choice=="3":
                result=calculator.product(num1,num2)
                print(f"The product of the numbers = {result}")
            elif choice=="4":
                result=calculator.divition(num1,num2)
                print(f"The division of the numbers = {result}")
        except ValueError:
            print("Please enter an integer")
        except ZeroDivisionError:
            print("divition by zero is not allowed")
main()






#Write a python program to implement a calculator
print("Select operation.")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
choice = input("Enter choice as (1/2/3/4):")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
            addition=num1+num2;
            print(num1, "+", num2, "=", addition)
elif choice == '2':
            subtraction=num1-num2;
            print(num1, "-", num2, "=", subtraction)
elif choice == '3':
            multiplication=num1*num2;
            print(num1, "*", num2, "=", multiplication)
elif choice == '4':
            division=num1/num2;
            print(num1, "/", num2, "=", division)
else:
        print("Invalid Input")
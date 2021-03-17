#Find the largest of three numbers

no1 = int(input("Enter first number: "))
no2 = int(input("Enter second number: "))
no3 = int(input("Enter third number: "))
if no1>no2:
    if no1>no3:
        print("No 1 is the largest number")
    else:
        print("No 3 is the largest number")
else:
    if no2>no3:
        print("No 2 is the largest number")
    else:
        print("No 3 is the largest number")    

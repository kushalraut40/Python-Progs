#Write a python program to calculate area of tringle, circle and rectangle. Take inputs from the user

print(" Enter c for circle, t for triangle, r for rectangle")    
choice = input("Enter the shape you want to calculate area of: ")
pie = 3.14
if choice == "c":
        radius = int(input("Enter the value of radius: "))
        area = 2 * pie * radius
elif choice == "t":
        base = int(input("Enter the value of base: "))
        height = int(input("Enter the value of height: "))
        area = 0.5 * base * height
elif choice=="r":
        l=int(input("Enter the legth of the rectangle:"))
        b=int(input("Enter the breadth of the rectangle:"))
        area==l*b;
else:
    print ("Select a valid shape")
print ("%.2f" % area)

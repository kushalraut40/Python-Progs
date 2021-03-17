#convert and print the distance in  meters, feet, inches and  centimeters. 

print("Enter the distance between two cities (in km) :")
km = float(input())
m = km*1000
feet = km * 3280.84
inch = km * 39370.1
cm = km * 100000
yard = km * 1093.61
print("\n Distance in Kilometres = ",km)
print("\n Distance in metres = ",m)
print("\n Distance in Feet = ",feet)
print("\n Distance in inches = ",inch)
print("\n Distance in centimetres = ",cm)
print("\n Distance in yards = ",yard)

#Write a python program to take string as input from the user, and display 0th character, 
# display 3rd to 6th character, display 6th character onwards, display last character, 
# print the string twice and concatenate two strings.

string=input("Enter a string of choice")
n =len(string);
print("0th character of the string is:")
print(string[0]);
print("3rd to 6th character of the string is:")
print(string[2:6]);
print("String from 6th character onwards is:")
print(string[5:]);
print("The last character of the string is:")
print(string[n-1]);
print("The string twice is:")
stringdouble=string+string;
print(stringdouble);
string1=input("Enter a string of choice to concatenate with old string")
string2=string+string1;
print(string2);
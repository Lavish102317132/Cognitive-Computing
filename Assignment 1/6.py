str=input("Enter the string")
vowels=0
for i in str:
    if i=='a' or i=='e'or i=='i' or i=='o' or i=='u':
        vowels=vowels+1
print(vowels)
str1=""
for i in str:  
    str1 = i + str1  
print(str1)
if str1==str:
    print("The string is palindrome")
else :
    print("The string is not palindrome")
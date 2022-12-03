"""Write a python script which takes a three digit number from the user and displays
only its last digit."""

a=int(input("enter a num:"))
if 99<a>999:
    print("error")
else:
    b=a%10
    print(b)
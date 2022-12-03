"""Write a python script which takes a three digit number from the user and displays
only its first digit."""

a=int(input("enter 3 digit num:"))
if 99<a>999:
    print("error")
else:
    b=int(a/100)
    print(b)



"""Write a python program to check whether a given string is a multiword string or single
word string using match case statement"""
a=input("enter a string:")
match a:
    case a if (" ") in a:
        print("multiword string")
    case a if ("") in a:
        print("singleword string")
"""Write a python program to check whether a given number is positive, negative or
zero using match case statement"""
a=int(input("enter num:"))
match a:
    case a if (a>0):
        print("num is positive")
    case a if (a<0):
        print("num is negative")
    case a if (a==0):
        print("num is zero")
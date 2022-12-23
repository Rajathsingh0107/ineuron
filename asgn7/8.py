"""Write a python script to check whether two given strings are identical, first string
comes before the second in dictionary order or first string comes after the second
string in dictionary order using match case statement"""
a=input("enter 1st string:")
b=input("enter 2nd string:")
match (a,b):
    case (a,b) if a==b:
        print("identical string")
    case (a,b) if a>b:
        print("{} comes before {}".format(a,b))
    case (a,b) if a<b:
        print("{} comes after {}".format(b,a))
    
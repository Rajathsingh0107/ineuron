"""Write a python script to print greater between two numbers. Print number only once
even if the numbers are the same."""
#method1
a=int(input("enter 1st num:"))
b=int(input("enter 2nd num:"))
if a>b:
    print(a)
else:
    print(b)

#method2
print("enter 2 num:")
a,b=int(input()),int(input())
print("greater num is",a if a>b else b)

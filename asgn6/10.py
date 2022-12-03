"""Write a python script to print greater among three numbers. Print number only once
even if the numbers are the same."""
#method1
a=int(input("enter 1st num:"))
b=int(input("enter 2nd num:"))
c=int(input("enter 3rd num:"))
if a<b<c:
    print("greater num is",c)
if a>b>c:
    print("greater num is",a)
if a<b>c:
    print("greater num is",b)
if a==b==c:
    print("all are equal:",a)

#method2
print("enter 3 num:")
a,b,c=int(input()),int(input()),int(input())
print("biggest num is",(a if a>c else c) if a>b  else(b if b>c else c))



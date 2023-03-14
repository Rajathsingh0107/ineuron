"""Write a python script to print the octal equivalent of a given decimal number. (do not
use oct() method)"""
#method1
n=int(input("enter decimal num:"))
l=list()
while n!=0:
    a=n%8
    l.append(a)
    n=n//8
l.reverse()
for e in l:
    print(e,end="")

#method2
a=141
print(oct(a))
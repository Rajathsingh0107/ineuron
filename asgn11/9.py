"""Write a python script to print binary equivalent of a given decimal number. (do not
use bin() method)"""
#method1
n=int(input("enter decimal num:"))
l=list()
while n!=0:
    a=n%2
    l.append(a)
    n=n//2
l.reverse()
for e in l:
    print(e,end="")

#method2
a=34
print(bin(a))

"""Write a python script to print first N terms of a Fibonacci series"""
a=int(input("enter:"))
b,c=0,1
sum=0
for i in range(0,a):
    print(sum)
    b=c
    c=sum
    sum=b+c

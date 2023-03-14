"""Write a python script to calculate sum of digits of a given number"""
a=int(input("enter no:"))
b=str(a)
print(sum([int(i) for i in b]))

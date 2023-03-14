"""Write a python script to calculate sum of squares of first N natural numbers"""
a=int(input("enter num:"))
sum=0
for i in range (a+1):
    sum=sum+(i*i)
print(sum)
"""Write a python script to calculate sum of cubes of first N natural numbers"""
a=int(input("enter no:"))
sum=0
for i in range(a+1):
    sum=sum+(i*i*i)
print(sum)

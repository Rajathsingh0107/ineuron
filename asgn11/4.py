"""Write a python script to calculate sum of first N odd natural numbers"""
a=int(input("enter no:"))
sum=0
for i in range(1,a+1):
    if i%2!=0:
        sum=sum+i
print(sum)
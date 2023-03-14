"""Write a python script to calculate factorial of a given number"""
a=int(input("no:"))
count=1
for i in range(a,0,-1):
    count=count*i
print(count)

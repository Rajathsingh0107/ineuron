"""Write a Python script to create a list of first N odd natural numbers."""
a=int(input("enter num:"))
l=[]
for i in range(1,a+1):
    if i%2!=0:
        l.append(i)
print(l)

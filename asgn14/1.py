"""Write a Python script to create a list of first N natural numbers."""
a=int(input("enter num:"))
l=[]
for i in range(1,a+1):
    l.append(i)
    i+=1
print(l)

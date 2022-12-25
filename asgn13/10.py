"""Write a Python script to create a list, where each element of the list is a digit of a
given number."""
a=int(input("no:"))
list=[]
b=str(a)
for i in b:
    list.append(int(i))
print(list)
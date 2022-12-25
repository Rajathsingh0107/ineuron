"""Write a Python script to create a list of city names taken from the user."""
m=int(input("enter no of cities:"))
list=[]
for i in range(m):
    a=input("enter name:")
    list.append(a)
print(list)
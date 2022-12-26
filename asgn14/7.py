"""Write a Python script to remove all non int values from a list."""
a=[1,2,3,5,8,"raj","taj","jar"]
b=[x for x in a if type(x)==int]
print(b)    
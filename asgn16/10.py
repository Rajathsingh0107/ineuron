"""Write a python program to change the first item (22) of a list within the following tuple
to 222.
tuple1 = (11, [22, 33], 44, 55)"""
tuple1 = (11, [22, 33], 44, 55)
l=[]
for i in tuple1:
    l.append(i)
l[1]=[222, 33]
tuple2=tuple(l)
print(tuple2)
print(type(tuple2))
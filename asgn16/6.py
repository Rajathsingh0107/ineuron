"""Write a python program to divide the tuple into four variables.
tuple1=(100, 200, 300, 400)"""
tuple1=(100, 200, 300, 400)
a, b, c, d = tuple1
print(a)
print(b)
print(c)
print(d)

#method1
a,b,c,d=(100, 200, 300, 400)
print(a,b,c,d)

#method2
tuple1=(100, 200, 300, 400)
a=0
for i in tuple1:
    a+=1
    print(a,i)

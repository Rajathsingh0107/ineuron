"""Write a python script to check whether a given quadratic equation has two real &
distinct roots, real & equal roots or imaginary roots"""
a=int(input("enter x square coefficient:"))
b=int(input("enter x coefficient:"))
c=int(input("enter constant value:"))
d=(b**2)-(4*a*c)
if d>0:
    print("real and distinct roots")
elif d<0:
    print("real and equal roots")
else:
    print("imaginary")
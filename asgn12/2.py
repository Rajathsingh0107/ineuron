"""Write a python script to check whether a given number is Prime or not"""
a=int(input("enter num:"))
for i in range(2,a):
    if a%i==0:
        print("not prime")
        break
else:
    print("prime")
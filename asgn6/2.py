"""Write a python script to check whether a given number is divisible by 5 or not"""
a=int(input("enter num:"))
if a%5==0:
    print("divisible by 5")
else:
    print("not divisible by 5")


#method2
print("num is divisible by 5" if int(input("enter num:"))%5==0 else "not divisible by 5")

"""Write a python script to check whether a given number is even or odd"""
#method1
a=int(input("enter num:"))
if a%2==0:
    print("its even")
else:
    print("its odd")


#method2
print("num is even" if int(input("enter num:"))%2==0 else "odd")

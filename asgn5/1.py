"""Write a python script to remove the last digit from a given number. (for example, if
user enters 2534 then your output should be 253)"""

#method1
a=2534
b=a//10
print(b)

#method2
a=int(input("enter num:"))
b=int(a/10)
print(b)
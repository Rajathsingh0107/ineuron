"""Write a python script to print MySirG N times on the screen"""
#method1
a="MySirG"
i=int(input("enter no of times:"))
b=0
while b<i:
    print(a)
    b+=1 

#method2
n=int(input("enter no of times:"))
i=1
while i<=n:
    print("mysirg")
    i+=1

#method3
n=int(input("enter no of times:"))
while n:#beacuse zero is false,and non zero value is true
    print("mysirg")
    n-=1


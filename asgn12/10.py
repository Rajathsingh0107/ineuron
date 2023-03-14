"""Write a python script to calculate HCF of two numbers"""

a=int(input("enter 1st num:"))
b=int(input("enter 2nd num:"))
l1=[]
for i in range(1,a):
        if a%i==0:
                l1.append(i)
print("factors of 1st num",l1)
l2=[]
for j in range(1,b):
        if b%j==0:
                l2.append(j)
print("factors of 2nd num",l2)
l=[]
for i in l1:
      for j in l2:
         if i==j:
             l.append(i)
print("hcf of 2 num's is",max(l))

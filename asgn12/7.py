"""Write a python script to check whether a given pair of numbers are co-Prime
numbers or not."""
a=int(input("enter 1st num:"))
b=int(input("enter 2nd num:"))
l1=[]
for i in range(1,a+1):
        if a%i==0:
                l1.append(i)
print("factors of 1st num",l1)
l1.remove(1)
l2=[]
for j in range(1,b+1):
        if b%j==0:
                l2.append(j)
print("factors of 2nd num",l2)
l2.remove(1)
out=0
for m in l1:
        if out==1:
                break
        for n in l2:
                if m==n:
                        print("not coprime")
                        out=1
if out==0:
        print("its coprime")

#                         continue
#                 else:
#                         break
# print("not")


        
                
"""Write a python script to print all Prime numbers between two given numbers (both
values inclusive)"""
a=int(input("enter 1st num"))
b=int(input("enter 2nd num"))
l=[]
for i in range(a,b+1):
    for m in range(2,i):
        if i%m==0:
            break
    else:
        l.append(i)
print(l)

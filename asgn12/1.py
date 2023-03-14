"""Write a python script to reverse a number."""
#method1
a=int(input("enter a num"))
l=str(a)
b=l[::-1]
print(b)

#method2
a=int(input("enter a num"))
l1=[]
for i in str(a):
    l1.append(i)
r=l[::-1]
print(r)

#method3
a=input("enter a num")
reverse=''
for i in range(len(a),0,-1):
    reverse+=a[i-1]
b=int(reverse)
print(b,type(b))







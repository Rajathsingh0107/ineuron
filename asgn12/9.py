"""Write a python script to calculate LCM of two numbers"""#inco
#method1
a=int(input("num1:"))
b=int(input("num2:"))
maxnum=max(a,b)
while True:
    if(maxnum%a==0 and maxnum%b==0):
        break
    maxnum=maxnum+maxnum
print(maxnum)

#method2
a=int(input("no1:"))
b=int(input("no2:"))
if a<b:
    higher=b
else:
    higher=a
    
while True:
    if (higher%a==0 and higher%b==0):
        break
    higher=higher+higher
print(higher)

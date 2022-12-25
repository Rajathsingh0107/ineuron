"""Write a python program to Print all items by referring to their index number (thislist =
["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]"""

#method1
thislist =["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
a=len(thislist)
i=0
b=1
while i<a:
    print(b,thislist[i])
    i+=1
    b+=1

#method2
thislist =["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]    
a=0
for i in thislist:
    a+=1
    print(a,i)



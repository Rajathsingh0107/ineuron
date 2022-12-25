"""Write a python script to store multiple items in a single variable ( Items are “Java”
,“Python”, “SQL”, “C” ) using list"""
#method1
a=["Java","Python","SQL","C"]
print(a)

#method2
a=input("names:")
l=[]
for i in a:
    l.append(i)
print(l)
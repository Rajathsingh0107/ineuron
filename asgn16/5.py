"""Write a python program to check if all items in the tuple are the same."""
#method1
a=("raj","taj","raj")
print(len(set(a))==1)

#method2
a=("raj","taj",1)
for i in a:
    if type(i)==str:
        continue
    if type(i)!=str:
        print("not same data type")

#method3
a=(1,1,"ra")
print(all(i==a[0] for i in a))


"""Write a python script to print first N even natural numbers"""
a=int(input("no:"))
i=2
while i<=a:
    if i%2==0:
        print(i)
    i+=1
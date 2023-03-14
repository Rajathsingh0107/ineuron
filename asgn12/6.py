"""Write a python script to print first N prime numbers"""
n=int(input("enter num:"))
for i in range(2,n):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,end= " ")

"""7. Write a python script to print first N odd natural numbers"""
a=int(input("enter num:"))
for i in range(1,a+1):
    if i%2!=0:
        print(i)
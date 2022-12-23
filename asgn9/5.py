"""Write a python script to print first N odd natural numbers in reverse order"""
max=int(input("enter a num:"))
while max:
    if max%2!=0:
        print(max)
    max-=1
    
"""Write a python script to check whether a given year is a leap year or not."""
a=int(input("enter year:"))
if a%400==0 or a%100!=0 and a%4==0: 
    print("leap")
else:
    print("not leap")
    
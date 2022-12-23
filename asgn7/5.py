"""Write a program which takes a number from user. Print Saurabh Shukla if the number
is even, print Prateek Jain if the number is negative odd number and print Aditya
Choudhary if number is positive odd number."""
a=int(input("enter a number:"))
match a:
    case a if (a%2==0) and (a>0):
        print("Saurabh Shukla") 
    case a if (a<0) and (a%2!=0):
        print("Prateek Jain") 
    case a if (a%2!=0) and (a>0):
        print("Aditya Choudhary") 
    case _:
        print("invalid input")
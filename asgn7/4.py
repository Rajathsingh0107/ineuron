"""Write a program which takes user’s age and display the category of person. Age
below 10 years- Kid, Age below 20 - Teen, Age below 40 - young, Age below 60 -
Experienced, Age above or equal 60 - Senior Citizen."""

a=int(input("enter age:"))
match a:
    case a if (a<10):
       print("kid")
    case a if (a<20):
       print("teen")
    case a if (a<40):
       print("young")
    case a if (a<60):
       print("experienced")
    case a if (a>=60):
       print("senior citizen")
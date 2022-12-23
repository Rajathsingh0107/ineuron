"""Write a python script to check whether a given year is
a. Non century leap year
b. Century leap year
c. Non century non leap year
d. century non leap year"""

a=int(input("enter year"))
match a:
    case a if (a%100!=0 and a%4==0):
        print("Non century leap year")
    case a if (a%100==0 and a%400==0):
        print("century leap year")
    case a if (a%100!=0 and a%4!=0):
        print("Non century non leap year")
    case a if (a%100==0 and a%400!=0):
        print("century non leap year")
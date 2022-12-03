"""Write a python script to take the month value in numeric format and display the
number of days in it."""
#method1
a=int(input("enter month num:"))
if a==1:
    print("january","31 days")
elif a==2:
    print("february","29/29 days")
elif a==3:
    print("march","31 days")
elif a==4:
    print("april","30 days")
elif a==5:
    print("may","31 days")
elif a==6:
    print("june","30 days")
elif a==7:
    print("july","31 days")
elif a==8:
    print("august","31 days")
elif a==9:
    print("sepetember","30 days")
elif a==10:
    print("october","31 days")
elif a==11:
    print("november","30 days")
elif a==12:
    print("december","31 days")
else:
    if a not in range(1,12):
        print("error")

#method2
month=int(input("enter a month:"))
if month in (1,3,5,7,8,10,12):
    print("31 days")
elif month in (4,6,9,11):
    print("30 days")
elif month==2:
    print("28/29 days")
else:
    if month not in range(1,12):
        print("error")





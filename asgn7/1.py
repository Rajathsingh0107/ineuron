# """Write a python script to display the number of days in a given month number."""
a=int(input("enter month num:"))
match a:
    case 1:
        print("january","31 days")
    case 2:
        print("february","29/29 days")
    case 3:
        print("march","31 days")
    case 4:
        print("april","30 days")
    case 5:
        print("may","31 days")
    case 6:
        print("june","30 days")
    case 7:
        print("july","31 days")
    case 8:
        print("august","31 days")
    case 9:
        print("sepetember","30 days")
    case 10:
        print("october","31 days")
    case 11:
        print("november","30 days")
    case 12:
        print("december","31 days")


# method2:
a=int(input("enter month number"))
match a:
    case a if  a in (1,3,5,7,8,10,12):
        print("31 days")
    case a if  a in (4,6,9,11):
        print("30 days")
    case 2:
        print("28/29 days")
    case _:
        print("invalid number")

 




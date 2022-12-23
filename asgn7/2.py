"""Write a menu driven program to perform following operations - Addition, Subtraction,
Multiplication, Division"""
a=int(input("enter 1st num:"))
b=int(input("enter 2nd num:"))
print("select operation:","1)addition","2)subtraction","3)multiply","4)divide",sep="\n")
c=int(input("enter operaton number:"))
match c:
    case 1:
        d=a+b
        print(d)
    case 2:
        d=a-b
        print(d)
    case 3:
        d=a*b
        print(d)
    case 4:
        d=a/b
        print(d)




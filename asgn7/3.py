"""Write a menu driven program with the following options:
a. Check whether a given set of three numbers are lengths of an isosceles
triangle or not
b. Check whether a given set of three numbers are lengths of sides of a right
angled triangle or not
c. Check whether a given set of three numbers are equilateral triangle or not
d. Exit."""
num1=int(input("num1:"))
num2=int(input("num2:"))
num3=int(input("num3:"))
print("1)check for isosceles triangle","2)check for right angled triangle","3)check for equilateral triangle",sep="\n")
choice=int(input("enter choice:"))
match choice:
    case 1:
        if num1==num2 or num1==num3 or num2==num3:
            print("isosceles triangle")
        else:
            print("not isosceles triangle")
    case 2:
        if (num1==90 or num2==90 or num3==90) or (num1+num2==90 or num1+num3==90 or num2+num3==90):
            print("right angle")
        else:
             print("not right angle")
    case 3:
        if num1==num2==num3:
            print("equilateral triangle")
        else:
            print("not equilateral")
    case _:
        print("error:choose correct option")
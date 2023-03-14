# """Write a python script to find next prime number of a given number"""
num = int(input("Enter a number: "))
while True:
    num+=1
    for i in range(2,num):
        if num%i==0:
            break
    else:
        print(num)
        break
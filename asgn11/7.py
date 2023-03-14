"""Write a python script to count digits in a given number"""
a=int(input("no:"))
count=0
b=str(a)
for i in b:
    count+=1
print("total digits are:",count)
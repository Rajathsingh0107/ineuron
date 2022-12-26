"""Write a python script to Get the characters from position 2 to position 5 (Given String
“Hello Learners” using the slice syntax)"""

#method1
a='''"Hello Learners"'''
while len(a)>1:
    for i in range(2,6):
        print(a[i])
    i+=1
    break

#method2
a='''"Hello Learners"'''
print(a[2:5])
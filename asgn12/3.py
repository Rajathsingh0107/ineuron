# """3. Write a python script to print all Prime numbers under 100"""
l=[]
for i in range(2,100):
    for n in range(2,i):
        if i%n==0:
                break
    else:
        l.append(i)
print(l)

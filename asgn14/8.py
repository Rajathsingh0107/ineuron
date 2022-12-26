"""Write a Python script to print distinct elements along with their frequencies of
occurrence in the list."""
list=[]
list2=[]
o=int(input("no of elements:"))
for i in range(o):
    a=input("enter elements for list:")
    for i in a:
        list.append(i)
print("original list:",list)
count=0
for r in list:
    if r in list2:
        count+=1
    if r not in list2:
        list2.append(r)
print("list without repetition:",list2)
print("no of times most frequent element repeated:",count)
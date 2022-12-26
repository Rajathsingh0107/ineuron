"""Write a Python script to print indices of all occurrences of a given element in a given
list."""
list=[1,2,3,4,1]
#element=1
size=len(list)
for r in range(size):
    if (list[r]==1):
        print(r)
        

"""Write a Python script to find the greatest number in a given list of numbers."""
#method1
l=[5,4,6,23,4,56,3,42,2]
l.sort()
print("sorted list is",l)
print("greatest num is:",l[-1])
print()

#method2
l=[5,4,6,23,4,56,3,42,2]
a=sorted(l)
print("sorted list is",a)
print("greatest num is:",a[-1])
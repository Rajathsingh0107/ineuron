"""Write a python script to display all prime numbers within a range.
# range
start = 15
end = 45"""
for i in range(15,45):
    for n in range(2,i):
        if i%n==0:
            break
    else:
        print(i)

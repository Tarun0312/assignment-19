# 8. Write a python program to multiply all the numbers in a list.

def multiply(l1):
    m=1
    for i in l1:
        m*=i
    return m    

print(multiply([2,4,5,6]))    
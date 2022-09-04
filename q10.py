# 10. Write a python program to create a function to check whether a given number is even
# or odd.

def checkEven(num):
    if(num%2):
        return 1
    return 0    

print("Odd" if(checkEven(eval(input("Enter a number: ")))==1) else "Even")   
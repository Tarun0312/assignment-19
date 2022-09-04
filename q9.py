# 9. Write a python program to create a function to check whether a number falls in a
# given range.

def range(num):
    if(0<=num<100):
        print("0-99")
    elif(100<=num<=999):
        print("100-999")  
    elif(1000<=num<=9999):
        print("1000-9999")
    elif(10000<=num<=99999):
        print("10000-99999") 
    else:
        print("1 Lakh and above")  
range(int(input("Enter a number: ")))                   
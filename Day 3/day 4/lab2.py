#Write a Python program to sum three given integers. However, if two or more values are equal sum will be zero.
a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=int(input("enter the third number"))
if a==b or b==c or c==a or a==b==c:
    print("zero")
else:
    d=a+b+c
    print(f"{d} is the sum")
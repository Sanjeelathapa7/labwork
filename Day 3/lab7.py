# Given a positive real number, print its fractional part. 
n=float(input("enter any number"))
import math
b=math.modf(n)
print(b)
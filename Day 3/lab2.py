#WAP which accepts marks of four subjects and display total marks, percentage and grade. 
# Hint: more than 70% –> distinction, more than 60% –> first, more than 40% –> pass, less than 40% –> fail 
a=int(input("enter marks of first subject "))
b=int(input("enter marks of second subject"))
c=int(input("enter marks of third subject"))
d=int(input("enter marks of fourth subject"))
n=((a+b+c+d)/400)*100
if n>70:
    print("distinction")
elif n>60:
    print("first")
elif n>40:
    print("pass")
elif n<40:
    print("fail")
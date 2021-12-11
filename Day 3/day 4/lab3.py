#Ask user to enter age, gender ( M or F ) and then using following rules print their place of service.
#if employee is female, then she will work only in urban areas.
#if employee is a male and age is in between 20 to 40 then he may work in anywhere
print("enter age")
age=int(input())
print("gender?(M or F")
gender=input()
if(gender=="F"or gender=="f")and 20<=age<=60:
    print("urban areas only")
elif(gender=="M"or gender=="m")and 40<age<=60:
    print("urban areas only")
else:
    print("ERROR")
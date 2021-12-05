#A school decides to replace te desks in three classroom,each desks sits two students.Given the number of students in each classroom print the smallest possible number of desks that can be purchased
a=int(input("enter the number of students in the first classroom"))
b=int(input("enter the number of students in the second classroom"))
c=int(input("enter the number of students in the third classroom"))
n=a/2+b/2+c/2
print(f"{n} number of desk should be purchased")
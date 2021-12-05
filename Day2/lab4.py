#N students takes K apples and distribute among each other evenly.The remaining(the invisible) part remains in the basket.How many apples will remain in the basket?The program reads the number N and K. It should print the two answers for the questions.
N=int(input("enter the number of students"))
K=int(input("enter the numbers of apples"))
a=int(K/N)
b=K-(a*N)
print(f"each student get {a} number of apples")
print(f"{b} apples are remaining in the basket")
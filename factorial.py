#prgm for factorial
n1=int(input("enter the value"))
fact=1
for i in range(1,n1+1):
    fact=fact*i
print(f"factorial of {n1} is {fact}")

a=int(input("Enter the first number\n"))
b=int(input("Enter the second number\n"))
ans = a - b
if ans < 0:
    ans = ans * (-1)
print(f"Difference of {a} and {b} is {ans}")
n1=int(input("Enter the number:"))
n = n1
num=0
while n != 0:
    r=n % 10
    num=num+( r ** 3)
    n //=10
if n1 == num:
    print(f"{n1} is an Armstrong number")
else:
    print(f"{n1} is not an Armstrong number")
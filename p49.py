#prgm to add 1 to each digit of given integer
n=int(input("Enter the number:"))
num,inc=0,0
while (n):
    r=n % 10
    num=num * 10 +( r + 1)
    n //=10
while (num):
    r=num % 10
    inc=inc * 10 +r
    num //=10
print(f"{inc}")
#prgm to find odd or even
n1=int(input("enter the no\n"))
if n1%2== 0:
    print(f"{n1} is even no")
else:
    print(f"{n1} is odd no")

#prgm for n natural no
n=int(input("enter the no\n"))
print("The natural nos are")
for i in range(1,n+1):
    print(i)

#prgm for n natural no in reverse order
n2=int(input("enter the no\n"))
print("The natural nos in reverse are")
for i in range(n,0,-1):
    print(i)
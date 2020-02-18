#prgm to find biggest no among 3
a=3
b=45
c=32
if a>b and a>c:
    print(f"Biggest no among {a},{b} and {c} is {a}")
elif b>c:
    print(f"Biggest no among {a},{b} and {c} is {b}")
else:
    print(f"Biggest no among {a},{b} and {c} is {c}")

#prgm to find biggest no among 2
n2=int(input("enter the first no\n"))
n3=int(input("enter the second no\n"))
if n2 > n3:
    print(f"The biggest of 2 nos entered ({n2} and {n3}) is {n2}")
else:
    print(f"The biggest of 2 nos entered ({n2} and {n3}) is {n3}")